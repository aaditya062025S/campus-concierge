import os
from typing import Dict, List
import asyncio
from scrapers.dining import get_dining_halls
from scrapers.bus import get_bus_times
from scrapers.clubs import get_club_events

# Note: LangChain setup removed for simplicity - using direct scraper calls instead

async def get_ai_response(query: str) -> Dict[str, any]:
    """
    Process a natural language query and return an AI-generated response
    with relevant campus information.
    """
    try:
        # Use the simplified response function
        return await get_simple_response(query)
        
    except Exception as e:
        # Fallback response if everything fails
        fallback_response = f"I'm sorry, I encountered an issue processing your question about '{query}'. "
        fallback_response += "Please try rephrasing your question or check the Virginia Tech website directly."
        
        return {
            "answer": fallback_response,
            "sources": ["https://vt.edu/"]
        }

# Alternative simpler approach without LangChain for basic functionality
async def get_simple_response(query: str) -> Dict[str, any]:
    """
    Simplified response function that directly calls scrapers based on keywords.
    """
    query_lower = query.lower()
    sources = []
    answer_parts = []
    
    # Check for dining-related queries
    if any(keyword in query_lower for keyword in ['dining', 'food', 'meal', 'eat', 'restaurant', 'open']):
        try:
            dining_data = await get_dining_halls()
            answer_parts.append(f"Dining Information: {dining_data}")
            sources.append("https://udc.vt.edu/")
        except Exception as e:
            answer_parts.append("Sorry, I couldn't fetch current dining information.")
    
    # Check for bus-related queries
    if any(keyword in query_lower for keyword in ['bus', 'transport', 'transit', 'ride']):
        try:
            bus_data = await get_bus_times()
            answer_parts.append(f"Bus Information: {bus_data}")
            sources.append("https://ridebt.org/")
        except Exception as e:
            answer_parts.append("Sorry, I couldn't fetch current bus information.")
    
    # Check for club-related queries
    if any(keyword in query_lower for keyword in ['club', 'event', 'activity', 'social']):
        try:
            events_data = await get_club_events()
            answer_parts.append(f"Club Events: {events_data}")
            sources.append("https://gobblerconnect.vt.edu/")
        except Exception as e:
            answer_parts.append("Sorry, I couldn't fetch current club events.")
    
    # If no specific topics identified, provide general help
    if not answer_parts:
        answer_parts.append("I can help you with dining, transportation, and club events at Virginia Tech. Please ask about specific topics!")
        sources = ["https://vt.edu/"]
    
    return {
        "answer": " ".join(answer_parts),
        "sources": sources
    }

