from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List, Optional
import uuid

from app.domain.crop_advisory.models import *
from app.domain.crop_advisory.schemas import *
from app.domain.crop_advisory.engine import *
from app.core.ai_agents import OllamaVLLMProvider, LangGraphAgenticPipeline

class CropAdvisoryLangGraphService:
    @staticmethod
    async def evaluate_async(db: AsyncSession, req: Any) -> Any:
        provider = OllamaVLLMProvider()
        pipeline = LangGraphAgenticPipeline(provider)
        agent_res = await pipeline.run_state_graph({"input": str(req)})
        return {"status": "SUCCESS", "agent_state": agent_res}
