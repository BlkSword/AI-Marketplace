from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI(
    title="FastAPI 示例服务",
    description="演示 FastAPI 基础功能",
    version="1.0.0"
)

# 定义数据模型
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# 模拟数据库
fake_db = {}

# 基础路由
@app.get("/")
async def read_root():
    return {"message": "欢迎使用 FastAPI"}

# 带路径参数的路由
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item 未找到")
    return {"item_id": item_id, "item": fake_db[item_id]}

# 带请求体的路由
@app.post("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    fake_db[item_id] = item
    return {"message": f"Item {item_id} 已创建", "item": item}

# 启动服务
if __name__ == "__main__":
    uvicorn.run(
        "main:app",  # 文件名:应用实例
        host="0.0.0.0",  # 监听地址
        port=8000,  # 监听端口
        reload=True  # 开发模式热重载
    )