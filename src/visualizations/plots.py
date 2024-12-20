# plots.py
import plotly.express as px
import plotly.graph_objects as go

from src.data.transformers import (
    producto_mas_ingresos,
    ranking_problemas,
    top_10_ejecutivos,
    porcentaje_estados,
    promedio_vida_util,
    producto_menor_vida_util,
    casos_por_mes
)

def plot_producto_mas_ingresos(data):
    producto = producto_mas_ingresos(data)
    fig = px.bar(
        producto,
        x='PRODUCTO',
        y='Total ingresos',
        title="Producto con más ingresos",
        labels={'PRODUCTO': 'Producto', 'Total ingresos': 'Ingresos'},
        color='Total ingresos',
        color_continuous_scale='Blues'
    )
    return fig

def plot_ranking_problemas(data):
    ranking = ranking_problemas(data)
    fig = px.bar(
        ranking,
        x='Total casos',
        y='Problema',
        title="Ranking de Problemas",
        labels={'Total casos': 'Total Casos', 'Problema': 'Problema'},
        color='Total casos',
        color_continuous_scale='Oranges'
    )
    return fig

def plot_casos_por_mes(data):
    casos = casos_por_mes(data)
    fig = px.bar(
        casos,
        x='Mes',
        y='Total casos',
        title="Casos por Mes",
        labels={'Mes': 'Mes', 'Total casos': 'Total Casos'},
        color='Total casos',
        color_continuous_scale='Jet'
    )
    return fig

def plot_top_10_ejecutivos(data):
    ejecutivos = top_10_ejecutivos(data)
    fig = px.bar(
        ejecutivos,
        x='Ejecutivo',
        y='Total casos',
        title="Top 10 Ejecutivos",
        labels={'Ejecutivo': 'Ejecutivo', 'Total ingresos': 'Ingresos'},
        color='Total casos',
        color_continuous_scale='Viridis'
    )
    return fig

def plot_porcentaje_estados(data):
    estados = porcentaje_estados(data)
    fig = px.pie(
        estados,
        names='Estado',
        values='Porcentaje',
        title="Porcentaje de Estados",
        color='Estado',
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    return fig


def plot_promedio_vida_util(data):
    # Obtener el promedio de vida útil
    promedio = promedio_vida_util(data)
    
    # Crear un gráfico de embudo (funnel chart)
    fig = go.Figure(
        data=[go.Funnel(
            y=['Promedio Vida Útil'],
            x=[promedio],
            textinfo='value+percent initial',  # Muestra valor y porcentaje
            marker=dict(color='#FF6347'),  # Color del embudo
        )]
    )
    
    # Personalización del gráfico
    fig.update_layout(
        title="Promedio de Vida Útil",
        showlegend=False
    )
    
    return fig

def plot_producto_menor_vida_util(data_limpia):
    producto_menor_vida = producto_menor_vida_util(data_limpia)
    fig = px.bar(
        producto_menor_vida,
        x='PRODUCTO',  # Ajusta a la columna correcta
        y='TIEMPO DE USO',  # Ajusta a la columna correcta
        title="Producto con Menor Vida Útil",
        labels={'PRODUCTO': 'Producto', 'TIEMPO DE USO': 'Tiempo de Uso'},
        color='TIEMPO DE USO',
        color_continuous_scale='YlGnBu'
    )
    return fig
