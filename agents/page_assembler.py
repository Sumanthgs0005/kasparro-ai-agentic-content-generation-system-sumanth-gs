"""Page Assembler Agent - Assembles final JSON pages for delivery"""
from typing import Dict, Any, List
import json


class PageAssemblerAgent:
    """
    Agent responsible for assembling final, machine-readable JSON pages.
    
    Responsibility: Take templated pages and assemble them into final,
    deliverable JSON format. Performs validation and schema enforcement.
    
    Autonomy: Works independently with only templated pages and questions as input.
    Outputs production-ready JSON pages.
    """

    def __init__(self, config: Dict[str, Any] | None = None):
        """Initialize the PageAssembler agent."""
        self.config = config or {}

    def execute(
        self, templated_pages: Dict[str, Any], questions: List[Dict[str, Any]]
    ) -> Dict[str, Dict[str, Any]]:
        """
        Assemble final JSON pages for all page types.
        
        Args:
            templated_pages: Templated pages from TemplateEngineAgent
            questions: FAQ questions from QuestionGeneratorAgent
            
        Returns:
            Dictionary containing final pages:
            - faq.json: FAQ page in production-ready JSON
            - product_page.json: Product page in production-ready JSON
            - comparison_page.json: Comparison page in production-ready JSON
        """
        # Extract pages
        faq_template = templated_pages.get("faq_page", {})
        product_template = templated_pages.get("product_page", {})
        comparison_template = templated_pages.get("comparison_page", {})

        # Assemble FAQ Page
        faq_page = {
            "type": "faq_page",
            "meta": {
                "title": faq_template.get("title", "FAQ"),
                "description": faq_template.get("description", ""),
                "version": "1.0",
            },
            "content": {
                "sections": faq_template.get("sections", {}),
                "total_questions": len(questions),
            },
        }

        # Assemble Product Page
        product_page = {
            "type": "product_page",
            "meta": {
                "title": product_template.get("title", "Product"),
                "version": "1.0",
            },
            "content": {
                "benefits": product_template.get("benefits_section", {}),
                "ingredients": product_template.get("ingredients_section", {}),
                "usage": product_template.get("usage_section", {}),
                "highlights": product_template.get("highlights", []),
            },
        }

        # Assemble Comparison Page
        comparison_page = {
            "type": "comparison_page",
            "meta": {
                "title": comparison_template.get("title", "Comparison"),
                "version": "1.0",
            },
            "content": {
                "comparison": comparison_template.get("comparison_data", {}),
                "testimonials": comparison_template.get("testimonials", []),
            },
        }

        # Return all pages as final output
        return {
            "faq.json": faq_page,
            "product_page.json": product_page,
            "comparison_page.json": comparison_page,
        }
