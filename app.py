from project_1.server import server
from crimes_yearly_trend import app as crimes_yearly_trend
from theft_analysis import app as theft_analysis
from top_crimes import app as top_crimes
 
@server.route('/')
def index():
    return crimes_yearly_trend.index()
 
 
if __name__ == "__main__":
    server.run(host="localhost", port=5000)
