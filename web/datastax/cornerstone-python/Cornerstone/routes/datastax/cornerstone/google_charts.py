from flask import Blueprint, render_template, request

gcharts_endpoint = Blueprint('gcharts_endpoint', __name__)


def compose_ajax_source():
    """
    grab request GET variables to create new url
    :return: ajax ready url
    """
    # grab url parameter, if available
    url = request.args.get('url', '/api/paging/system/compaction_history')

    # pass all other parameters to ajax url
    ajax_source = '%s?' % url
    for k, v in request.args.iteritems():
        if k != 'url':
            ajax_source += '&%s=%s' % (k, v)

    return ajax_source


@gcharts_endpoint.route('/annotationchart/')
def annotationchart():
    ajax_source = compose_ajax_source()

    return render_template('general/charts/google-charts/google-charts.jinja2',
                           ajax_source=ajax_source,
                           gcharts_version=1,
                           packages='annotationchart',
                           data_method='DataTable(jsonData.gcharts[1.1])',
                           chart_type='visualization.AnnotationChart',
                           options='options')


@gcharts_endpoint.route('/areachart/')
def areachart():
    ajax_source = compose_ajax_source()

    return render_template('general/charts/google-charts/google-charts.jinja2',
                           ajax_source=ajax_source,
                           gcharts_version=1,
                           packages='corechart',
                           data_method='arrayToDataTable('
                                       'jsonData.gcharts[1])',
                           chart_type='visualization.AreaChart',
                           options='options')


@gcharts_endpoint.route('/barchart/')
def barchart():
    ajax_source = compose_ajax_source()

    return render_template('general/charts/google-charts/google-charts.jinja2',
                           ajax_source=ajax_source,
                           gcharts_version=1.1,
                           packages='bar',
                           data_method='DataTable(jsonData.gcharts[1.1])',
                           chart_type='charts.Bar',
                           options='google.charts.Bar.convertOptions(options)')


@gcharts_endpoint.route('/linechart/')
def linechart():
    ajax_source = compose_ajax_source()

    return render_template('general/charts/google-charts/google-charts.jinja2',
                           ajax_source=ajax_source,
                           gcharts_version=1.1,
                           packages='line',
                           data_method='DataTable(jsonData.gcharts[1.1])',
                           chart_type='charts.Line',
                           options='google.charts.Line.convertOptions(options)')


@gcharts_endpoint.route('/piechart/')
def piechart():
    ajax_source = compose_ajax_source()

    return render_template('general/charts/google-charts/google-charts.jinja2',
                           ajax_source=ajax_source,
                           gcharts_version=1,
                           packages='corechart',
                           data_method='arrayToDataTable('
                                       'jsonData.gcharts[1])',
                           chart_type='visualization.PieChart',
                           options='options')


@gcharts_endpoint.route('/table/')
def table():
    ajax_source = compose_ajax_source()

    return render_template('general/charts/google-charts/google-charts.jinja2',
                           ajax_source=ajax_source,
                           gcharts_version=1,
                           packages='table',
                           data_method='arrayToDataTable('
                                       'jsonData.gcharts[1])',
                           chart_type='visualization.Table',
                           options='options')
