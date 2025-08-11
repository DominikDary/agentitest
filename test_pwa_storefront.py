import allure
import pytest

from conftest import BaseAgentTest


@allure.feature("Navigation Menu")
class TestNavigationMenu(BaseAgentTest):
    """Tests the navigation menu structure and links."""

    @allure.story("Top Header Navigation")
    @allure.title("Test Navigation Menu Contains Required Items")
    @pytest.mark.asyncio
    async def test_navigation_menu_items(self, llm, browser_session):
        """Tests that the top header navigation contains 'New Arrivals', 'Man', and 'Woman'."""
        task = "look at the top header navigation bar and verify that it contains 'New Arrivals', 'Man', and 'Woman'. Return 'navigation_items_found' if all three are present."
        await self.validate_task(
            llm, browser_session, task, "navigation_items_found", ignore_case=True
        )


@allure.feature("Product Catalog")
class TestProductCatalog(BaseAgentTest):
    """Tests product catalog functionality and product details."""

    @allure.story("Top Sellers Section")
    @allure.title("Test Top Sellers Contains Lego Indiana Jones")
    @pytest.mark.asyncio
    async def test_top_sellers_lego_product(self, llm, browser_session):
        """Tests that Top Sellers section contains the Lego Indiana Jones product."""
        task = "navigate to the 'Top Sellers' section and verify that the list contains 'Lego Indian Jones: The Original Adventure (for Wii) $49.99'. Return 'lego_product_found' if it is present."
        await self.validate_task(
            llm, browser_session, task, "lego_product_found", ignore_case=True
        )

    @allure.story("Product Details Page")
    @allure.title("Test Product Details Delivery Options")
    @pytest.mark.asyncio
    async def test_product_delivery_options(self, llm, browser_session):
        """Tests that clicking on the Lego product shows delivery options with 'Ship to Address' selected."""
        task = "navigate to 'Top Sellers', click on the 'Lego Indian Jones: The Original Adventure (for Wii) $49.99' product, and verify that on the product details page the delivery option selection shows 'Ship to Address'. Return 'ship_to_address_found' if it is present."
        await self.validate_task(
            llm, browser_session, task, "ship_to_address_found", ignore_case=True
        )