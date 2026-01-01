"""Data Parser Agent - Parses and normalizes raw product data"""
from pydantic import BaseModel
import json
from typing import Dict, Any, List


class DataParserAgent:
    """
    Agent responsible for parsing and normalizing raw product JSON data.
    
    Responsibility: Transform raw unstructured product data into a normalized,
    standardized internal format that other agents can reliably consume.
    
    Autonomy: Operates independently with no global state. Input and output
    are well-defined dictionaries, making the agent testable and reusable.
    """

    def __init__(self, config: Dict[str, Any] | None = None):
        """Initialize the DataParser agent with optional configuration."""
        self.config = config or {}

    def execute(self, raw_product_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Parse and normalize raw product data.
        
        Args:
            raw_product_data: Raw product JSON from input source
            
        Returns:
            Normalized product dictionary with standardized keys:
            - product_name
            - concentration
            - skin_type
            - ingredients
            - benefits
            - usage_instructions
            - side_effects
            - price
            - competitor_products
        """
        normalized = {
            "product_name": raw_product_data.get("name", "Unknown Product"),
            "concentration": raw_product_data.get("concentration", ""),
            "skin_type": raw_product_data.get("skin_type", []),
            "ingredients": raw_product_data.get("ingredients", []),
            "benefits": raw_product_data.get("benefits", []),
            "usage_instructions": raw_product_data.get("usage", ""),
            "side_effects": raw_product_data.get("side_effects", ""),
            "price": raw_product_data.get("price", ""),
            "competitor_products": raw_product_data.get("competitor_products", {}),
        }
        return normalized
