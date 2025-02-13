class PrometheusNotFound(Exception):
    """Exception, when Prometheus cannot be reached"""


class NoPrometheusUrlFound(Exception):
    """Exception, when Prometheus url is incorrect"""

    pass


class VictoriaMetricsNotFound(Exception):
    """Exception, when VictoriaMetrics cannot be reached"""

    pass


class AlertsManagerNotFound(Exception):
    """Exception, when AlertManager cannot be reached"""

    pass


class NoAlertManagerUrlFound(Exception):
    """Exception, when AlertManager url is incorrect"""

    pass

class PrometheusFlagsConnectionError(Exception):
    """Exception, when Prometheus flag or AlertManager flag api cannot be reached"""

