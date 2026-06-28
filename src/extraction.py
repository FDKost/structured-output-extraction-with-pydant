import os
from typing import Union

from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.runnables import RunnablePassthrough

from .schemas import PersonInfo, MeetingNotes
from .utils import select_schema

load_dotenv()  # Load OPENAI_API_KEY from .env

def get_llm(model_name: str = "gpt-3.5-turbo", temperature: float = 0.0):
    return OpenAI(model=model_name, temperature=temperature)

def extract_info(
    text: str,
    llm,
    schema_type: type = None,
) -> Union[PersonInfo, MeetingNotes]:
    """
    Extract structured data from free‑text using LangChain and Pydantic.
    """
    if schema_type is None:
        schema_type = select_schema(text)

    parser = PydanticOutputParser(pydantic_object=schema_type)

    prompt = PromptTemplate(
        input_variables=["text"],
        template=(
            "Extract the following information from the text:\n\n{text}\n\n"
            "Respond in JSON format following the schema:\n{schema_description}"
        ),
    )

    chain = (
        RunnablePassthrough.assign(
            schema_description=lambda _: parser.schema_description
        )
        | prompt
        | llm
        | parser
    )

    try:
        result = chain.invoke({"text": text})
    except Exception as e:
        raise RuntimeError(f"LLM or parser failed: {e}") from e

    return result
