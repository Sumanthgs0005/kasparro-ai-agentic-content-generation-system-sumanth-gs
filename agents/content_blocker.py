"""Content Blocker Agent - Creates reusable content blocks from product data"""
from typing import Dict, Any, List


class ContentBlockAgent:
    """
    Agent responsible for creating reusable content blocks from parsed product data and FAQs.
    
    Responsibility: Transform raw product information and questions into structured,
    reusable content blocks (benefits, ingredients, usage, comparisons) that can be
    mapped to different page templates.
    
    Autonomy: Operates independently. Receives parsed product and FAQ questions,
    outputs content blocks with no side effects.
    """

    def __init__(self, config: Dict[str, Any] | None = None):
        """Initialize the ContentBlock agent."""
        self.config = config or {}

    def execute(
        self, parsed: Dict[str, Any], questions: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Create reusable content blocks from product data and FAQs.
        
        Args:
            parsed: Normalized product data from DataParserAgent
            questions: FAQ questions from QuestionGeneratorAgent
            
        Returns:
            Dictionary of content blocks:
            - benefits_block: Product benefits structured
            - ingredients_block: Ingredient information
            - usage_block: Usage instructions structured
            - comparison_block: Competitive comparison info
            - faq_blocks: FAQ questions organized by category
        """
        product_name = parsed.get("product_name", "Product")
        benefits = parsed.get("benefits", [])
        ingredients = parsed.get("ingredients", [])
        usage = parsed.get("usage_instructions", "")
        competitors = parsed.get("competitor_products", {})

        # Create Benefits Block
        benefits_block = {
            "type": "benefits",
            "title": f"Why Choose {product_name}?",
            "items": [
                {"benefit": benefit, "description": f"{benefit} tailored for your skin"}
                for benefit in benefits
            ],
        }

        # Create Ingredients Block
        ingredients_block = {
            "type": "ingredients",
            "title": "Key Ingredients",
            "items": [
                {"name": ingredient, "type": "Natural Extract"}
                for ingredient in ingredients
            ],
        }

        # Create Usage Block
        usage_block = {
            "type": "usage",
            "title": "How to Use",
            "steps": [
                {"step": 1, "instruction": "Cleanse your skin thoroughly"},
                {"step": 2, "instruction": "Apply a small amount of serum"},
                {"step": 3, "instruction": f"{usage if usage else 'Massage gently until absorbed'}"},
                {"step": 4, "instruction": "Follow with your regular moisturizer"},
            ],
        }

        # Create Comparison Block
        comparison_block = {
            "type": "comparison",
            "title": "How We Compare",
            "our_product": product_name,
            "competitors": list(competitors.keys()) if competitors else [],
            "advantages": [
                "Natural ingredients",
                "Clinically tested",
                "Cruelty-free",
                "Fast-absorbing formula",
            ],
        }

        # Create FAQ Blocks organized by category
        faq_by_category = {}
        for question in questions:
            category = question.get("category", "General")
            if category not in faq_by_category:
                faq_by_category[category] = []
            faq_by_category[category].append(
                {"question": question.get("question"), "id": question.get("id")}
            )

        faq_blocks = {
            "type": "faqs",
            "title": "Frequently Asked Questions",
            "categories": faq_by_category,
        }

        return {
            "benefits_block": benefits_block,
            "ingredients_block": ingredients_block,
            "usage_block": usage_block,
            "comparison_block": comparison_block,
            "faq_blocks": faq_blocks,
        }
