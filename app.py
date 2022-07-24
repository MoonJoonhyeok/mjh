import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go

import numpy as np
import matplotlib.pyplot as plt

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

template='plotly_white'

# 그래프1
area=['전국', '인구감소지역(평균)', '관심지역(평균)','울산광역시 울진군']
y=[20, 14, 23,28]

# 그래프2
y_0 = [5,6,5,6,5,6,7,8,9,10,11,12]
y_1 = [11,12,16,18,12,15,12,12,14,12,12,12]

x = ['01월','02월','03월','04월','05월','06월','07월','08월','09월','10월','11월','12월']

# 그래프3
y_01 = [5,6,5,6,5,6,7,8,9,10,11,12]
y_02 = [11,12,16,18,12,15,12,12,14,12,12,12]
y_03 = [5,6,5,6,5,6,7,8,9,10,11,12]
y_04 = [11,12,16,18,12,15,12,12,14,12,12,12]
y_05 = [5,6,5,6,5,6,7,8,9,10,11,12]
y_06 = [11,12,16,18,12,15,12,12,14,12,12,12]

x_01 = ['01월','02월','03월','04월','05월','06월','07월','08월','09월','10월','11월','12월']

# 그래프4
city=['서울특별시','부산광역시','대구광역시','인천광역시','광주광역시','대전광역시','울산광역시','제주특별자치도','경기도','강원도','충청북도','충청남도','전라북도','전라남도','경상북도','경상남도','제주특별자치도']
use =[3.7,77.1,0.9,0.8,0.3,0.4,1.6,0.1,3.7,0.3,0.5,0.4,0.3,0.5,1.3,7.7,0.5]
marker_color=('mediumspringgreen','teal','lime','steelblue','lightsteelblue','dodgerblue','aqua','midnightblue','orange','crimson'
             ,'violet','plum','mistyrose','thistle','slateblue','blanchedalmond','goldenrod','lightpink')
             
             app = dash.Dash(__name__)

#1
fig = go.Figure([go.Bar(x=area, y=y ,marker_color=('black','darkgray','lightgrey', 'darkblue'),text=y, textposition='auto')])

fig.update_layout(height=500, width=800, showlegend=False, template=template)
fig.update_layout(title={'text': "(단위:영유아 천 명당)",'y':0.82,'x':0.78,'xanchor': 'center','yanchor': 'top'})
fig.update_layout(title_font_size=18)
fig.update_yaxes(showline=True, linewidth=2, gridwidth=3, linecolor='white', gridcolor='lightgray')

#2
fig1 = go.Figure([go.Bar(x=area, y=y ,marker_color=('black','darkgray','lightgrey', 'darkblue'),text=y, textposition='auto')])

fig1.update_layout(height=500, width=800, showlegend=False, template=template)
fig1.update_layout(title={'text': "(단위:학생 천 명당)",'y':0.82,'x':0.78,'xanchor': 'center','yanchor': 'top'})
fig1.update_layout(title_font_size=18)
fig1.update_yaxes(showline=True, linewidth=2, gridwidth=3, linecolor='white', gridcolor='lightgray')

#3
fig2 = go.Figure([go.Bar(x=area, y=y ,marker_color=('black','darkgray','lightgrey', 'darkblue'),text=y, textposition='auto')])

fig2.update_layout(height=500, width=800, showlegend=False, template=template)
fig2.update_layout(title={'text': "(단위:아동 만 명당)",'y':0.82,'x':0.78,'xanchor': 'center','yanchor': 'top'})
fig2.update_layout(title_font_size=18)
fig2.update_yaxes(showline=True, linewidth=2, gridwidth=3, linecolor='white', gridcolor='lightgray')

#4
fig3 = go.Figure([go.Bar(x=area, y=y ,marker_color=('black','darkgray','lightgrey', 'darkblue'),text=y, textposition='auto')])

fig3.update_layout(height=500, width=800, showlegend=False, template=template)
fig3.update_layout(title={'text': "(단위:노인 만 명당)",'y':0.82,'x':0.78,'xanchor': 'center','yanchor': 'top'})
fig3.update_layout(title_font_size=18)
fig3.update_yaxes(showline=True, linewidth=2, gridwidth=3, linecolor='white', gridcolor='lightgray')

#5
fig4 = go.Figure([go.Bar(x=area, y=y ,marker_color=('black','darkgray','lightgrey', 'darkblue'),text=y, textposition='auto')])

fig4.update_layout(height=500, width=800, showlegend=False, template=template)
fig4.update_layout(title={'text': "(단위:인구 천 명당)",'y':0.82,'x':0.78,'xanchor': 'center','yanchor': 'top'})
fig4.update_layout(title_font_size=18)
fig4.update_yaxes(showline=True, linewidth=2, gridwidth=3, linecolor='white', gridcolor='lightgray')

#6
fig5 = go.Figure([go.Bar(x=area, y=y ,marker_color=('black','darkgray','lightgrey', 'darkblue'),text=y, textposition='auto')])

fig5.update_layout(height=500, width=800, showlegend=False, template=template)
fig5.update_layout(title={'text': "(단위:인구 만 명당)",'y':0.82,'x':0.78,'xanchor': 'center','yanchor': 'top'})
fig5.update_layout(title_font_size=18)
fig5.update_yaxes(showline=True, linewidth=2, gridwidth=3, linecolor='white', gridcolor='lightgray')

#8
fig6 = go.Figure()
fig6.add_trace(go.Bar(x=x,y=y_0,name='청년연령(만19시-34세)',marker=dict(color='rgb(102, 178, 255)'),text=y_0, textposition='auto'))
fig6.add_trace(go.Bar(x=x,y=y_1,name='그외연령',marker=dict(color='rgb(204, 229, 255)'),text=y_1, textposition='auto'))

fig6.update_layout(barmode='stack')
fig6.update_layout(yaxis_title='인구이동량 (단위:천 명)')
fig6.update_layout(xaxis_title='2021년')
fig6.update_layout(legend_title_text='울산광역시 울진군 연령대구분')
fig6.update_layout(height=500, width=800, template=template)
fig6.update_yaxes(showline=True, linewidth=2, gridwidth=3, linecolor='white', gridcolor='lightgray')

#7
fig7= go.Figure(data=go.Scatterpolar(r=[1, 5, 2, 2, 3,8,12,15,16,24,26,25,21,20,30,21,22,21,31,21,21,21,21,21,],
                                     theta=['18','19','20','21','22','23','0/24','1','2','3','4','5','6','7','8','9','10',
                                            '11','12','13','14','15','16','17'],
                                     fill='toself'))
fig7.update_layout(title={'text': "울산광역시 울진군 시간대별 청년 활동인구%",'y':0.9,'x':0.5,'xanchor': 'center','yanchor': 'top'})
fig7.update_layout(polar=dict(radialaxis=dict(visible=True)),showlegend=False)
fig7.update_layout(height=500, width=800,template=template)

fig7.update_polars(angularaxis_gridwidth=0.1)
fig7.update_polars(angularaxis_griddash='dash')
fig7.update_polars(angularaxis_gridcolor='gray')

fig7.update_polars(radialaxis_color='gray')
fig7.update_polars(radialaxis_griddash='dash')
fig7.update_polars(radialaxis_showgrid=True)
fig7.update_polars(radialaxis_gridwidth=0.9)


#9
fig8 = go.Figure()
fig8.add_trace(go.Bar(x=x_01,y=y_01,name='생활서비스',marker=dict()))
fig8.add_trace(go.Bar(x=x_01,y=y_02,name='소매/유통',marker=dict()))
fig8.add_trace(go.Bar(x=x_01,y=y_03, name='여가/오락',marker=dict()))
fig8.add_trace(go.Bar(x=x_01,y=y_04,name='음식',marker=dict( )))
fig8.add_trace(go.Bar(x=x_01,y=y_05,name='의료/건강',marker=dict( )))
fig8.add_trace(go.Bar(x=x_01,y=y_06,name='기타',marker=dict(color='rgb(204, 229, 255)')))

fig8.update_layout(barmode='stack')
fig8.update_layout(yaxis_title='매출액 (백만원 당)')
fig8.update_layout(xaxis_title='2021년')
fig8.update_layout(legend_title_text='울산광역시 울진군 6대 업종분류')
fig8.update_layout(height=500, width=800, template=template)

# 0
fig9 = go.Figure()
fig9.add_trace(go.Bar(y=city,x=use,orientation="h",marker_color=marker_color,text=use, textposition='auto'))

fig9.update_layout(barmode='stack')
fig9.update_layout(yaxis_title='거주광역시도')
fig9.update_layout(xaxis_title='부산광역시 중구-2021년 매출액 시도별 분포%')
fig9.update_layout(height=600, width=1000, template=template)
fig9.update_layout(modebar_orientation='h')

fig9.update_xaxes(showline=True, linewidth=3, linecolor='white', gridcolor='white')
fig9.update_yaxes(showline=True, linewidth=2, gridwidth=3, linecolor='white', gridcolor='lightgray')
fig9.update_layout(font=dict(size=18))


app.layout = html.Div(children=[
    html.H1(children='인구감소지역 주요 현황', style={'text-align': 'center'}),
    html.P(children='인구감소지역 주요 현황', style={'text-align': 'center'}),
    html.Div(children='접근성 평가기준 : 국토교통부, 2019, “지역의 기초생활인프라 공급 현황 자료 및 분석 안내서” 참고'),

    html.Div([
        html.Label(['관련지표'], style={'font-weight': 'bold'}),
        dcc.Dropdown(
            id='dropdown',
            options=[
                {'label': '어린이집·유치원 수(2021)', 'value': 'graph1'},
                {'label': '초·중·고교 수(2021)', 'value': 'graph2'},
                {'label': '아동복지시설 수(2021)', 'value': 'graph3'},
                {'label': '노인복지시설 수(2021)', 'value': 'graph4'},
                {'label': '의료시설 수(2021)', 'value': 'graph5'},
                {'label': '문화·체육시설 수(2021)', 'value': 'graph6'},
                {'label': '[총 활동인구 및 청년 활동인구]', 'value': 'graph7'},
                {'label': '[시간대별 청년 활동인구]', 'value': 'graph8'},
                {'label': '[월별·업종별 카드 매출액]', 'value': 'graph9'},
                {'label': '[거주지(광역시도)별 카드 매출액]', 'value': 'graph10'}],value='graph1',style={"width": "60%"}),

        html.Div(dcc.Graph(id='graph'))])])


@app.callback(
    Output('graph', 'figure'),
    [Input(component_id='dropdown', component_property='value')]
)
def select_graph(value):
    if value == 'graph1':
        return fig
    elif value == 'graph2':
        return fig1
    elif value == 'graph3':
        return fig2
    elif value == 'graph4':
        return fig3
    elif value == 'graph5':
        return fig4
    elif value == 'graph6':
        return fig5
    elif value == 'graph7':
        return fig6
    elif value == 'graph8':
        return fig7
    elif value == 'graph9':
        return fig8
    elif value == 'graph10':
        return fig9

server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)
