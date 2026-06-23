from utils.logger import get_logger

logger = get_logger()


def test_login(driver):

    logger.info("Opening login page")

    driver.get(
        "https://the-internet.herokuapp.com/login"
    )

    logger.info("Entering credentials")

