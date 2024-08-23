from fastapi import APIRouter

import api_models


router = APIRouter(tags = ['copy'])


@router.post('/', response_model = api_models.Route1_Res)
async def get_resonse(request_data: api_models.Route1_Req):

    response = {
        "status": "success",
        "message": "Matching ad copy assets retrieved successfully.",
    }

    return response
