"""
Tests for MoldBot Manufacturing
"""

import pytest
from moldbot_manufacturing import MoldBotManufacturing


@pytest.fixture
def system():
    """Create system instance for tests"""
    return MoldBotManufacturing()


def test_initialization(system):
    """Test system initialization"""
    assert system.version == "1.0.0"
    assert system.status == "Pilot"


def test_process(system):
    """Test process function"""
    result = system.process({"test": "input"})
    
    assert result["status"] == "success"
    assert result["project"] == "MoldBot Manufacturing"
    assert result["version"] == "1.0.0"


def test_info(system):
    """Test get_info function"""
    info = system.get_info()
    
    assert info["name"] == "MoldBot Manufacturing"
    assert info["version"] == "1.0.0"
    assert info["type"] == "manufacturing"


@pytest.mark.asyncio
async def test_async_process(system):
    """Test async process"""
    result = await system.process_async({"test": "async"})
    assert result["status"] == "success"
