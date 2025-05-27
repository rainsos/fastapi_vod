from typing import Annotated

from pydantic import BaseModel, Field

from app.dtos.frozen_config import FROZEN_CONFIG


class CreateMeetingResponse(BaseModel):
    model_config = FROZEN_CONFIG
    url_code: Annotated[str, Field(description="회의 URL 코드. unique 합니다.")]
