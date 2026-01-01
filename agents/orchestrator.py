"""Orchestrator Agent - Central coordinator for multi-agent workflow"""
from typing import Dict, Any, List
from agents.data_parser import DataParserAgent
from agents.question_generator import QuestionGeneratorAgent
from agents.content_blocker import ContentBlockAgent
from agents.template_engine import TemplateEngineAgent
from agents.page_assembler import PageAssemblerAgent


class Orchestrator:
    """
    Central coordinator that manages the multi-agent workflow.
    
    Responsibilities:
    - Encodes workflow as a Directed Acyclic Graph (DAG)
    - Dynamically routes data between agents
    - Maintains shared state dictionary
    - Provides clear agent boundaries and orchestration logic
    """

    def __init__(self):
        """Initialize all agents as independent, modular components."""
        self.data_parser = DataParserAgent()
        self.question_gen = QuestionGeneratorAgent()
        self.content_blocker = ContentBlockAgent()
        self.template_engine = TemplateEngineAgent()
        self.page_assembler = PageAssemblerAgent()

        # Define workflow as a DAG (Directed Acyclic Graph)
        # Each node represents an agent, edges represent data flow
        self.workflow_graph = [
            "parse_data",
            "generate_questions",
            "create_content_blocks",
            "apply_templates",
            "assemble_pages",
        ]

    def run(self, raw_product_json: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the multi-agent workflow orchestration.
        
        Args:
            raw_product_json: Raw product data JSON
            
        Returns:
            Dict containing final pages: {"faq", "product_page", "comparison_page"}
        """
        # Shared state dictionary passed between agents
        state: Dict[str, Any] = {"raw_product": raw_product_json}

        # Execute each node in the workflow DAG
        for node in self.workflow_graph:
            if node == "parse_data":
                # Agent 1: Parse and normalize raw product data
                state["parsed_product"] = self.data_parser.execute(state["raw_product"])

            elif node == "generate_questions":
                # Agent 2: Generate FAQ questions from parsed data
                state["questions"] = self.question_gen.execute(state["parsed_product"])

            elif node == "create_content_blocks":
                # Agent 3: Create reusable content blocks
                state["content_blocks"] = self.content_blocker.execute(
                    parsed=state["parsed_product"], questions=state["questions"]
                )

            elif node == "apply_templates":
                # Agent 4: Apply page-specific templates to content blocks
                state["templated_pages"] = self.template_engine.execute(
                    content_blocks=state["content_blocks"]
                )

            elif node == "assemble_pages":
                # Agent 5: Assemble final JSON pages for each page type
                state["final_pages"] = self.page_assembler.execute(
                    templated_pages=state["templated_pages"],
                    questions=state["questions"],
                )

        return state["final_pages"]
