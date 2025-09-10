from src.logger import get_logger
from src.custom_exception import CustomException
import sys

logger = get_logger(__name__)

def test_divide(a, b):
    try:
        result = a / b
        logger.info(f"Division successful: {a} / {b} = {result}")
        return result
    except Exception as e:
        logger.error("Error occurred during division")
        raise CustomException("Custom Error zero", sys)
    
if __name__ == "__main__":
    try:
        logger.info("Starting test cases")
        test_divide(10, 0)
    except CustomException as ce:
        logger.error(f"Caught an exception: {ce}")

    try:
        logger.info("Starting test cases")
        test_divide(10, 2)
    except CustomException as ce:
        logger.error(f"Caught an exception: {ce}")