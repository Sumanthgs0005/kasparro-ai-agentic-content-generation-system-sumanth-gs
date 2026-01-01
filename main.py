#!/usr/bin/env python3
"""
Kasparro Applied AI Challenge - Refactored Multi-Agent System

This main.py demonstrates the orchestrated multi-agent architecture:
- DataParserAgent: Normalizes raw product data
- QuestionGeneratorAgent: Generates 16 FAQ questions
- ContentBlockAgent: Creates reusable content blocks
- TemplateEngineAgent: Maps blocks to page templates
- PageAssemblerAgent: Assembles final JSON pages
- Orchestrator: Coordinates all agents via DAG workflow
"""

import json
import os
from pathlib import Path
from agents.orchestrator import Orchestrator

# Sample product data
PRODUCT_DATA = {
    "name": "GlowBoost Vitamin C Serum",
    "concentration": "10% Vitamin C",
    "skin_type": ["Oily", "Combination"],
    "ingredients": ["Vitamin C", "Hyaluronic Acid"],
    "benefits": ["Brightening", "Fades dark spots"],
    "usage": "Apply 2-3 drops in the morning before sunscreen",
    "side_effects": "Mild tingling for sensitive skin",
    "price": "$699",
    "competitor_products": {"Competitor A": "Similar formula", "Competitor B": "Higher price"},
}


def main():
    """
    Execute the multi-agent orchestration workflow.
    
    The Orchestrator manages the entire workflow:
    1. Parse raw product data (DataParserAgent)
    2. Generate FAQ questions (QuestionGeneratorAgent)
    3. Create content blocks (ContentBlockAgent)
    4. Apply page templates (TemplateEngineAgent)
    5. Assemble final pages (PageAssemblerAgent)
    """
    print("\n" + "="*60)
    print("🤖 KASPARRO MULTI-AGENT ORCHESTRATION SYSTEM")
    print("="*60)

    # Initialize the Orchestrator (which manages all agents)
    orchestrator = Orchestrator()
    print("\n✓ Orchestrator initialized with 5 autonomous agents")
    print("  - DataParserAgent")
    print("  - QuestionGeneratorAgent")
    print("  - ContentBlockAgent")
    print("  - TemplateEngineAgent")
    print("  - PageAssemblerAgent")

    # Execute the DAG workflow
    print("\n" + "-"*60)
    print("Executing multi-agent workflow via Directed Acyclic Graph...")
    print("-"*60)
    
    pages = orchestrator.run(PRODUCT_DATA)
    
    print("\n✓ Workflow completed successfully!")

    # Save output files
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    print("\nSaving generated pages:")
    for filename, page_data in pages.items():
        filepath = output_dir / filename
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(page_data, f, indent=2, ensure_ascii=False)
        print(f"  ✓ {filepath}")

    print("\n" + "="*60)
    print("✓ Multi-agent system execution complete!")
    print("="*60)
    print()


if __name__ == "__main__":
    main()
