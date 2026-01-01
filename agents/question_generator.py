"""Question Generator Agent - Generates FAQ questions from product data"""
from typing import Dict, Any, List


class QuestionGeneratorAgent:
    """
    Agent responsible for generating FAQ questions from normalized product data.
    
    Responsibility: Generate comprehensive, categorized FAQ questions that address
    customer concerns about the product. Returns 16 questions across key topics.
    
    Autonomy: Works independently with only the parsed product data as input.
    No global state or external dependencies.
    """

    def __init__(self, config: Dict[str, Any] | None = None):
        """Initialize the QuestionGenerator agent."""
        self.config = config or {"num_questions": 16}
        self.categories = [
            "Product Overview",
            "Usage Instructions",
            "Benefits & Results",
            "Ingredients & Safety",
        ]

    def execute(self, parsed_product: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Generate 16 FAQ questions from parsed product data.
        
        Args:
            parsed_product: Normalized product data from DataParserAgent
            
        Returns:
            List of 16 FAQ question dictionaries, each containing:
            - id: Unique question identifier
            - category: FAQ category
            - question: The FAQ question text
            - context: Product-specific context used to generate this question
        """
        product_name = parsed_product.get("product_name", "Product")
        benefits = parsed_product.get("benefits", [])
        ingredients = parsed_product.get("ingredients", [])
        usage = parsed_product.get("usage_instructions", "")
        side_effects = parsed_product.get("side_effects", "")

        faqs = [
            # Product Overview - 4 questions
            {
                "id": 1,
                "category": "Product Overview",
                "question": f"What is {product_name}?",
                "context": f"{product_name} is a specialized skincare product.",
            },
            {
                "id": 2,
                "category": "Product Overview",
                "question": f"What are the main benefits of {product_name}?",
                "context": f"Benefits include: {', '.join(benefits[:3]) if benefits else 'improved skin health'}.",
            },
            {
                "id": 3,
                "category": "Product Overview",
                "question": f"Who should use {product_name}?",
                "context": "This product is suitable for various skin types.",
            },
            {
                "id": 4,
                "category": "Product Overview",
                "question": f"Is {product_name} suitable for sensitive skin?",
                "context": "Formulated with gentle, natural ingredients.",
            },
            # Usage Instructions - 4 questions
            {
                "id": 5,
                "category": "Usage Instructions",
                "question": f"How do I use {product_name}?",
                "context": f"Usage: {usage if usage else 'Apply as directed on packaging.'}",
            },
            {
                "id": 6,
                "category": "Usage Instructions",
                "question": f"How often should I use {product_name}?",
                "context": "Recommended frequency depends on your skin type.",
            },
            {
                "id": 7,
                "category": "Usage Instructions",
                "question": f"Can I use {product_name} with other products?",
                "context": "Generally compatible with most skincare routines.",
            },
            {
                "id": 8,
                "category": "Usage Instructions",
                "question": f"When will I see results from {product_name}?",
                "context": "Results typically appear within 2-4 weeks of consistent use.",
            },
            # Benefits & Results - 4 questions
            {
                "id": 9,
                "category": "Benefits & Results",
                "question": f"What specific skin concerns does {product_name} address?",
                "context": f"Targets: {', '.join(benefits) if benefits else 'multiple skin concerns'}.",
            },
            {
                "id": 10,
                "category": "Benefits & Results",
                "question": f"Are the benefits of {product_name} permanent?",
                "context": "Continued use maintains the benefits for your skin.",
            },
            {
                "id": 11,
                "category": "Benefits & Results",
                "question": f"Can I combine {product_name} with other treatments?",
                "context": "Yes, with proper guidance. Consult dermatologist if needed.",
            },
            {
                "id": 12,
                "category": "Benefits & Results",
                "question": f"What do users say about {product_name}?",
                "context": "Customers report positive results and high satisfaction.",
            },
            # Ingredients & Safety - 4 questions
            {
                "id": 13,
                "category": "Ingredients & Safety",
                "question": f"What are the key ingredients in {product_name}?",
                "context": f"Main ingredients: {', '.join(ingredients[:4]) if ingredients else 'Natural plant extracts and vitamins'}.",
            },
            {
                "id": 14,
                "category": "Ingredients & Safety",
                "question": f"Is {product_name} safe for all skin types?",
                "context": "Dermatologist-tested and hypoallergenic formula.",
            },
            {
                "id": 15,
                "category": "Ingredients & Safety",
                "question": f"Are there any side effects of {product_name}?",
                "context": f"Side effects: {side_effects if side_effects else 'Minimal. Some users may experience mild tingling.'}",
            },
            {
                "id": 16,
                "category": "Ingredients & Safety",
                "question": f"Is {product_name} cruelty-free and vegan?",
                "context": "Committed to ethical, sustainable production.",
            },
        ]

        return faqs
