# Tweak gevent and grpc so they work together:
# https://github.com/grpc/grpc/issues/4629#issuecomment-376962677

# Make the standard library cooperate with gevent.
# http://www.gevent.org/api/gevent.monkey.html
from gevent import monkey
monkey.patch_all()

# This must be called AFTER the python standard lib has been patched, but BEFORE creating and gRPC objects.
# https://github.com/grpc/grpc/blob/v1.32.x/src/python/grpcio/grpc/experimental/gevent.py
import grpc.experimental.gevent as grpc_gevent
grpc_gevent.init_gevent()
