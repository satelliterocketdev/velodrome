#!/bin/sh
set -e

dumb-init -- uwsgitop "$VELODROME_UWSGI_PORT_9191_TCP_ADDR:$VELODROME_UWSGI_PORT_9191_TCP_PORT"
