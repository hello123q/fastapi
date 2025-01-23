from fastapi import Request, APIRouter

router = APIRouter(prefix='/orders', tags=['orders'])

@router.get('/')
async def get_orders(request: Request):
    try:
        return {"message": "Working fine", "success": True}
    except Exception as e:
        return {"error": str(e), "success": False}