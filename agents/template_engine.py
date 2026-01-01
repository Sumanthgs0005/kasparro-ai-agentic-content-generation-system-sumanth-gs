"""Template Engine Agent - Maps content blocks to page-specific templates"""
from typing import Dict, Any


class TemplateEngineAgent:
    """
    Agent responsible for mapping generic content blocks to page-specific templates.
    
    Responsibility: Take reusable content blocks and apply them to specific page
    layouts (FAQ page, Product page, Comparison page).
    
    Autonomy: Works independently with only content blocks as input.
    Outputs templated pages ready for assembly.
    """

    def __init__(self, config: Dict[str, Any] | None = None):
        """Initialize the TemplateEngine agent."""
        self.config = config or {}

    def execute(self, content_blocks: Dict[str, Any]) -> Dict[str, Any]:
        """
        Apply content blocks to page-specific templates.
        
        Args:
            content_blocks: Content blocks from ContentBlockAgent
            
        Returns:
            Dictionary of templated pages:
            - faq_page: FAQ page with questions organized by category
            - product_page: Product showcase page
            - comparison_page: Competitive comparison page
        """
        # Extract blocks
        benefits = content_blocks.get("benefits_block", {})
        ingredients = content_blocks.get("ingredients_block", {})
        usage = content_blocks.get("usage_block", {})
        comparison = content_blocks.get("comparison_block", {})
        faqs = content_blocks.get("faq_blocks", {})

        # Template 1: FAQ Page
        faq_page = {
            "page_type": "faq",
            "title": "Frequently Asked Questions",
            "description": "Find answers to common questions about our product",
            "sections": faqs.get("categories", {}),
        }

        # Template 2: Product Page
        product_page = {
            "page_type": "product",
            "title": "Product Overview",
            "benefits_section": benefits,
            "ingredients_section": ingredients,
            "usage_section": usage,
            "highlights": [
                "Premium Formula",
                "Dermatologist Tested",
                "Cruelty-Free",
                "Fast-Acting Results",
            ],
        }

        # Template 3: Comparison Page
        comparison_page = {
            "page_type": "comparison",
            "title": "Why Choose Us?",
            "comparison_data": comparison,
            "testimonials": [
                "Trusted by skincare professionals",
                "Used by thousands of satisfied customers",
                "Award-winning formula",
            ],
        }

        return {
            "faq_page": faq_page,
            "product_page": product_page,
            "comparison_page": comparison_page,
        }
