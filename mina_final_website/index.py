import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from textwrap import dedent
from app import app
from apps import app1, search


app.index_string = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Mina's Website</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>
  {%metas%}
  {%favicon%}
  {%css%}
</head>

<body>
  <nav class="navbar navbar-expand-md bg-dark navbar-dark">
    <a class="navbar-brand" href="/" style=  'font-size:18px;'   >MINA LEE</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="collapsibleNavbar">
      <ul class="navbar-nav">
        <li class="nav-item" style= 'padding-top:10px;' >
          <a class="nav-link" href="/apps/search" style=  'font-size:18px;' >Project: Travel Recommendations</a>
        </li>
      </ul>
    </div>  
  </nav>
  <br>
  <div class="container">
    {%app_entry%}
  </div>
  <footer>
    {%config%}
    {%scripts%}
  </footer>
</body>
</html>
'''




app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),


])
index_page = html.Div([
    html.Iframe(
        width='101%',
        height='855px',
        style={'border' : '0px', 'padding-left' : '30px', 'padding-top':'30px'},
        sandbox='',
        srcDoc='''
          <h2>MINA LEE &nbsp; &nbsp; &nbsp; <img  src="https://www.dropbox.com/s/j1jgca26ax89c3u/image2.png?dl=1" style='width: 100px; height=150px; border-radius: 20px'/></h2>           
          <p></p>
          <p style="font-size: 18px;">I’m fascinated by unlocking insights from complex data sets, and keen to delve into efficient models and algorithms for applications to real-life problems. </p>
          <p> </p>
          <p><span style="text-decoration: underline;"><b>EDUCATION&nbsp; &nbsp; &nbsp;                                      </b></span></p>
          <p><strong>New York University<br /></strong>&nbsp; July, 2018 - Present (Dec, 2018)<br />&nbsp; Computer Science Bridge Program<strong><br /></strong></p>
          <p><strong>Yonsei University<br /></strong>&nbsp; August, 2014<br />&nbsp; Bachelor of Applied Statistics</p>
          <p><span style="text-decoration: underline;"><strong>WORK EXPERIENCE                            </strong></span></p>
          <p><strong>Track Revenue</strong><br />&nbsp; Product Manager <br />&nbsp; April, 2018 - Present</p>
          <p> </p>
          <p><strong>LG Uplus</strong><br />&nbsp; Data Analyst<br />&nbsp; July, 2014 - May, 2017</p>
          </ul>
          <p></p>
          <p><span style="text-decoration: underline;"><strong>RELEVANT COURSEWORK                </strong> </span>                                          </p>
          <ul>
            <li>Data structure and Algorithms, Computer Operating Systems, Discrete Mathematics, Computer Programming <g class="gr_ gr_371 gr-alert gr_gramm gr_inline_cards gr_run_anim Style multiReplace" id="371" data-gr-id="371" style="color: #222222; font-size: 15px;">C++ ,</g> Programming Fundamentals Java</li>
            <li>Regression Analysis, Computer Programming, Experimental Design, Mathematical Statistics, Sampling Theory, Nonparametric Statistics, Statistical Method, Calculus, Linear Algebra</li>
          </ul>
          <p></p>
          <p><span style="text-decoration: underline;"><strong>TECHNICAL SKILLS                           </strong></span></p>
          <ul>
            <li>Programming Languages: Python, Java, C++, SQL, HTML</li>
            <li>Software: R, SPSS, SAS, Git, Django, Dash, Databases (MySQL, RedShift, MongoDB), AWS</li>
          </ul>
          <p></p>
          <p><span style="text-decoration: underline;"><strong>LANGUAGES&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</strong></span></p>
          <ul>
            <li>Korean (Native), English (Fluent), Spanish (Beginner)</li>
          </ul>

        '''
    ),
    html.Div([

        html.A(html.Img(src='https://www.dropbox.com/s/btou08bnekhk5pr/github.png?dl=1',style={'height' : '55px','width' : '55px', 'padding': '5px'}),href='https://github.com/achievermina?tab=repositories', target = '_blank'),

        html.A(html.Img(src='https://www.dropbox.com/s/tbm3qs8ad2cq9zp/linkedin.png?dl=1',
                        style={'height': '55px', 'width': '55px', 'padding': '5px'}),
                        href='https://www.linkedin.com/in/mina-lee-67aa5312a/', target='_blank')

    ], style = {'padding-left': '40px', 'margin-bottom':'70px' })


])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/app1':
         return app1.layout
    elif pathname == '/apps/search':
         return search.layout
    else:
        return index_page

if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0", port=80)

