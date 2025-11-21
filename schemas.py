"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Literal

# Example schemas (keep for reference):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Agent builder schemas

ProviderType = Literal["openai", "anthropic", "openrouter", "meta", "google"]

class Agent(BaseModel):
    """
    Agents collection schema
    Collection name: "agent"
    """
    name: str = Field(..., description="Agent display name")
    provider: ProviderType = Field(..., description="LLM provider")
    model: str = Field(..., description="Model name, e.g., gpt-4o, claude-3-5-sonnet")
    system_prompt: str = Field("You are a helpful AI agent.", description="System instruction for the agent")
    color: str = Field("#7c3aed", description="Accent color hex for UI theming")
    temperature: float = Field(0.7, ge=0, le=2, description="Sampling temperature")

class ChatMessage(BaseModel):
    """
    Messages collection schema (optional, for transcripts)
    Collection name: "chatmessage"
    """
    agent_id: str = Field(..., description="Related agent id")
    role: Literal["system", "user", "assistant"]
    content: str

# Add your own schemas here:
# --------------------------------------------------

# Note: The Flames database viewer will automatically:
# 1. Read these schemas from GET /schema endpoint
# 2. Use them for document validation when creating/editing
# 3. Handle all database operations (CRUD) directly
# 4. You don't need to create any database endpoints!
