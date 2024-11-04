from opentelemetry import trace, metrics
from opentelemetry.exporter.prometheus import PrometheusMetricReader
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.metrics import Counter, Meter, MeterProvider
from backend.api import router
import asyncio

from fastapi import FastAPI
from backend.auth.auth.api import auth_app
from backend.msocket.msocket.msocket import main as socketserver

app = FastAPI()
# app.add_middleware()


@app.get("/")
async def root():
    return "it works!"


app.mount("", auth_app, "auth")  # app.add_middleware()


@app.get("/")
async def root():
    return "it works!"


app.mount("", auth_app, "auth")

if __name__ == "__main__":
    # 设置追踪提供者
    trace.set_tracer_provider(TracerProvider())
    tracer = trace.get_tracer(__name__)

    metrics.set_meter_provider(MeterProvider())
    meter = metrics.get_meter(__name__)

    # 配置 PrometheusMetric 导出器
    exporter = PrometheusMetricReader(MeterProvider())

    trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(exporter))
    # router()
    asyncio.run(socketserver())
