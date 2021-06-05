from fastapi import FastAPI, UploadFile
from fastapi.params import File
from loguru import logger
from minio import S3Error
from starlette.responses import JSONResponse

from s3_adapter.adapter import S3Adapter

app = FastAPI()


@app.post("/images")
def push_image(image: UploadFile = File(...)):
    s3_adapter = S3Adapter()

    try:
        s3_adapter.push_file("images", image.filename, image.file.fileno())
        return JSONResponse(
            status_code=201,
            content={
                "message": "Изображения успешно загружены. Подробнее http://localhost:9000/minio"
            },
        )
    except S3Error as e:
        logger.error(e)

        return JSONResponse(
            status_code=500, content={"message": "Ошибка на стороне S3"}
        )
    except Exception as e:
        logger.error(e)
        return JSONResponse(
            status_code=500, content={"message": "Внутренняя ошибка сервера"}
        )
