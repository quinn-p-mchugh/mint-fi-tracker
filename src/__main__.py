from datetime import date, timedelta
import plotly.express as px
from life import Life
from housing import housing
from income import income
from retirement import retirement
from taxes import taxes

cashflows = housing + income + retirement + taxes

today = date.today()
life = Life(date(2022, 2, 12), cashflows=cashflows)
forecast = life.generate_financial_forecast(
    today, today + timedelta(days=365 * 20)
)

fig = px.line(
    forecast,
    x=forecast.index,
    y="Cumulative Sum",
    title="Financial Independence Forecast",
)
fig.show()
