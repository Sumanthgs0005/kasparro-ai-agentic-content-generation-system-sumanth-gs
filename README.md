# Kasparro Applied AI Engineer Challenge
## Multi-Agent Content Generation System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)

**Transforms raw product data into structured marketing content via 6 specialized agents**

## 🎯 Overview
Takes GlowBoost Vitamin C Serum data → Generates 3 machine-readable JSON pages:
- **FAQ Page** (16 categorized questions)
- **Product Page** (benefits, usage, pricing)  
- **Comparison Page** (vs fictional PureGlow Serum)

## 🚀 Quick Demo


## 🏗️ Multi-Agent Architecture (Refactored)

### Addressing Assignment Requirements

This system has been refactored to meet the Kasparro Applied AI challenge requirements:

✅ **Clear Separation of Agent Responsibilities**
- Each agent is an independent, modular Python class
- Agents have well-defined input/output interfaces
- No agent contains monolithic or hard-coded logic

✅ **Dynamic Agent Interaction and Coordination**
- Orchestrator manages agents via a Directed Acyclic Graph (DAG)
- State flows through agents via explicit data dictionaries
- Workflow can be extended with new agents

✅ **Agent Autonomy**
- Agents operate independently with no global state
- Agents are testable, reusable components
- Agents support configuration without modification

### Agent Responsibilities

#### 1. **DataParserAgent**
- **Input**: Raw product JSON
- **Output**: Normalized product data
- **Responsibility**: Parse and structure raw product information

#### 2. **QuestionGeneratorAgent**
- **Input**: Normalized product data
- **Output**: 16 FAQ questions (4 categories × 4 questions)
- **Responsibility**: Generate comprehensive FAQ questions

#### 3. **ContentBlockAgent**
- **Input**: Parsed product data + FAQ questions
- **Output**: Reusable content blocks
- **Responsibility**: Create structured content blocks for multiple pages

#### 4. **TemplateEngineAgent**
- **Input**: Content blocks
- **Output**: Page-specific templated content
- **Responsibility**: Map generic blocks to page templates (FAQ, Product, Comparison)

#### 5. **PageAssemblerAgent**
- **Input**: Templated pages + questions
- **Output**: Final machine-readable JSON pages
- **Responsibility**: Assemble production-ready page JSON

### Orchestration: Directed Acyclic Graph (DAG)

```
Raw Product Data
       ↓
[DataParserAgent] → Parsed Product
       ↓
[QuestionGeneratorAgent] → FAQ Questions
       ↓ (both inputs)
[ContentBlockAgent] → Content Blocks
       ↓
[TemplateEngineAgent] → Templated Pages
       ↓
[PageAssemblerAgent] → Final JSON Pages
```

The **Orchestrator** class manages this DAG:
- Instantiates all agents
- Defines workflow sequence
- Routes data between agents
- Maintains shared state dictionary

### How This Differs From Hard-Coded Systems

**Before**: `main.py` called agents directly in sequential order with hard-coded variable names.

**After**: 
- Orchestrator manages the workflow
- Agents communicate via clean interfaces (dicts)
- Workflow is defined declaratively in the DAG
- Easy to add/remove/reorder agents
- Easy to test agents independently
