import click
import requests
from pydantic import ValidationError

from commands.converters.pdf_converter import PDFConverter
from logs.logger import logger


@click.command()
@click.argument('file_path', type=click.Path(exists=True))
@click.argument('file_id', type=str)
def pdf_xml(file_path, file_id):
    """This function converts a file from PDF
        to XML

    Args:
        file_path (file path): First parameter
        file_id (string): Second parameter
    Returns:
        Creates an XML file in the directory xmls_sciencebeam
    """
    try:
        converter = PDFConverter()
        xml_content = converter.convert(file_path)
        # Save the converted xml contents
        with open(f'docs/examples/sciencebeam_xml_outputs/{file_id}.xml', 'w', encoding='utf-8') as xml_file:
            xml_file.write(xml_content)
            logger.info(f'Converted: {file_path} with ID: {file_id} to XML')

    except ValidationError as error:
        logger.error("Validation error:", error)

    except requests.RequestException as error:
        logger.error("Request error:", error)
