# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/tasks_v2beta3/proto/target.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/tasks_v2beta3/proto/target.proto",
    package="google.cloud.tasks.v2beta3",
    syntax="proto3",
    serialized_options=_b(
        "\n\036com.google.cloud.tasks.v2beta3B\013TargetProtoP\001Z?google.golang.org/genproto/googleapis/cloud/tasks/v2beta3;tasks"
    ),
    serialized_pb=_b(
        '\n-google/cloud/tasks_v2beta3/proto/target.proto\x12\x1agoogle.cloud.tasks.v2beta3\x1a\x1cgoogle/api/annotations.proto"g\n\x12\x41ppEngineHttpQueue\x12Q\n\x1b\x61pp_engine_routing_override\x18\x01 \x01(\x0b\x32,.google.cloud.tasks.v2beta3.AppEngineRouting"\xc1\x02\n\x14\x41ppEngineHttpRequest\x12;\n\x0bhttp_method\x18\x01 \x01(\x0e\x32&.google.cloud.tasks.v2beta3.HttpMethod\x12H\n\x12\x61pp_engine_routing\x18\x02 \x01(\x0b\x32,.google.cloud.tasks.v2beta3.AppEngineRouting\x12\x14\n\x0crelative_uri\x18\x03 \x01(\t\x12N\n\x07headers\x18\x04 \x03(\x0b\x32=.google.cloud.tasks.v2beta3.AppEngineHttpRequest.HeadersEntry\x12\x0c\n\x04\x62ody\x18\x05 \x01(\x0c\x1a.\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"T\n\x10\x41ppEngineRouting\x12\x0f\n\x07service\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x10\n\x08instance\x18\x03 \x01(\t\x12\x0c\n\x04host\x18\x04 \x01(\t*[\n\nHttpMethod\x12\x1b\n\x17HTTP_METHOD_UNSPECIFIED\x10\x00\x12\x08\n\x04POST\x10\x01\x12\x07\n\x03GET\x10\x02\x12\x08\n\x04HEAD\x10\x03\x12\x07\n\x03PUT\x10\x04\x12\n\n\x06\x44\x45LETE\x10\x05\x42p\n\x1e\x63om.google.cloud.tasks.v2beta3B\x0bTargetProtoP\x01Z?google.golang.org/genproto/googleapis/cloud/tasks/v2beta3;tasksb\x06proto3'
    ),
    dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR],
)

_HTTPMETHOD = _descriptor.EnumDescriptor(
    name="HttpMethod",
    full_name="google.cloud.tasks.v2beta3.HttpMethod",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="HTTP_METHOD_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="POST", index=1, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="GET", index=2, number=2, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="HEAD", index=3, number=3, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="PUT", index=4, number=4, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="DELETE", index=5, number=5, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=622,
    serialized_end=713,
)
_sym_db.RegisterEnumDescriptor(_HTTPMETHOD)

HttpMethod = enum_type_wrapper.EnumTypeWrapper(_HTTPMETHOD)
HTTP_METHOD_UNSPECIFIED = 0
POST = 1
GET = 2
HEAD = 3
PUT = 4
DELETE = 5


_APPENGINEHTTPQUEUE = _descriptor.Descriptor(
    name="AppEngineHttpQueue",
    full_name="google.cloud.tasks.v2beta3.AppEngineHttpQueue",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="app_engine_routing_override",
            full_name="google.cloud.tasks.v2beta3.AppEngineHttpQueue.app_engine_routing_override",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=107,
    serialized_end=210,
)


_APPENGINEHTTPREQUEST_HEADERSENTRY = _descriptor.Descriptor(
    name="HeadersEntry",
    full_name="google.cloud.tasks.v2beta3.AppEngineHttpRequest.HeadersEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="google.cloud.tasks.v2beta3.AppEngineHttpRequest.HeadersEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="google.cloud.tasks.v2beta3.AppEngineHttpRequest.HeadersEntry.value",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=_b("8\001"),
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=488,
    serialized_end=534,
)

_APPENGINEHTTPREQUEST = _descriptor.Descriptor(
    name="AppEngineHttpRequest",
    full_name="google.cloud.tasks.v2beta3.AppEngineHttpRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="http_method",
            full_name="google.cloud.tasks.v2beta3.AppEngineHttpRequest.http_method",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="app_engine_routing",
            full_name="google.cloud.tasks.v2beta3.AppEngineHttpRequest.app_engine_routing",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="relative_uri",
            full_name="google.cloud.tasks.v2beta3.AppEngineHttpRequest.relative_uri",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="headers",
            full_name="google.cloud.tasks.v2beta3.AppEngineHttpRequest.headers",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="body",
            full_name="google.cloud.tasks.v2beta3.AppEngineHttpRequest.body",
            index=4,
            number=5,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[_APPENGINEHTTPREQUEST_HEADERSENTRY],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=213,
    serialized_end=534,
)


_APPENGINEROUTING = _descriptor.Descriptor(
    name="AppEngineRouting",
    full_name="google.cloud.tasks.v2beta3.AppEngineRouting",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="service",
            full_name="google.cloud.tasks.v2beta3.AppEngineRouting.service",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="version",
            full_name="google.cloud.tasks.v2beta3.AppEngineRouting.version",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="instance",
            full_name="google.cloud.tasks.v2beta3.AppEngineRouting.instance",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="host",
            full_name="google.cloud.tasks.v2beta3.AppEngineRouting.host",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=536,
    serialized_end=620,
)

_APPENGINEHTTPQUEUE.fields_by_name[
    "app_engine_routing_override"
].message_type = _APPENGINEROUTING
_APPENGINEHTTPREQUEST_HEADERSENTRY.containing_type = _APPENGINEHTTPREQUEST
_APPENGINEHTTPREQUEST.fields_by_name["http_method"].enum_type = _HTTPMETHOD
_APPENGINEHTTPREQUEST.fields_by_name[
    "app_engine_routing"
].message_type = _APPENGINEROUTING
_APPENGINEHTTPREQUEST.fields_by_name[
    "headers"
].message_type = _APPENGINEHTTPREQUEST_HEADERSENTRY
DESCRIPTOR.message_types_by_name["AppEngineHttpQueue"] = _APPENGINEHTTPQUEUE
DESCRIPTOR.message_types_by_name["AppEngineHttpRequest"] = _APPENGINEHTTPREQUEST
DESCRIPTOR.message_types_by_name["AppEngineRouting"] = _APPENGINEROUTING
DESCRIPTOR.enum_types_by_name["HttpMethod"] = _HTTPMETHOD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AppEngineHttpQueue = _reflection.GeneratedProtocolMessageType(
    "AppEngineHttpQueue",
    (_message.Message,),
    dict(
        DESCRIPTOR=_APPENGINEHTTPQUEUE,
        __module__="google.cloud.tasks_v2beta3.proto.target_pb2",
        __doc__="""App Engine HTTP queue.
  
  The task will be delivered to the App Engine application hostname
  specified by its
  [AppEngineHttpQueue][google.cloud.tasks.v2beta3.AppEngineHttpQueue] and
  [AppEngineHttpRequest][google.cloud.tasks.v2beta3.AppEngineHttpRequest].
  The documentation for
  [AppEngineHttpRequest][google.cloud.tasks.v2beta3.AppEngineHttpRequest]
  explains how the task's host URL is constructed.
  
  Using
  [AppEngineHttpQueue][google.cloud.tasks.v2beta3.AppEngineHttpQueue]
  requires
  ```appengine.applications.get`` <https://cloud.google.com/appengine/docs/admin-api/access-control>`_
  Google IAM permission for the project and the following scope:
  
  ``https://www.googleapis.com/auth/cloud-platform``
  
  
  Attributes:
      app_engine_routing_override:
          Overrides for the [task-level app\_engine\_routing][google.clo
          ud.tasks.v2beta3.AppEngineHttpRequest.app\_engine\_routing].
          If set, ``app_engine_routing_override`` is used for all tasks
          in the queue, no matter what the setting is for the [task-
          level app\_engine\_routing][google.cloud.tasks.v2beta3.AppEngi
          neHttpRequest.app\_engine\_routing].
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.tasks.v2beta3.AppEngineHttpQueue)
    ),
)
_sym_db.RegisterMessage(AppEngineHttpQueue)

AppEngineHttpRequest = _reflection.GeneratedProtocolMessageType(
    "AppEngineHttpRequest",
    (_message.Message,),
    dict(
        HeadersEntry=_reflection.GeneratedProtocolMessageType(
            "HeadersEntry",
            (_message.Message,),
            dict(
                DESCRIPTOR=_APPENGINEHTTPREQUEST_HEADERSENTRY,
                __module__="google.cloud.tasks_v2beta3.proto.target_pb2"
                # @@protoc_insertion_point(class_scope:google.cloud.tasks.v2beta3.AppEngineHttpRequest.HeadersEntry)
            ),
        ),
        DESCRIPTOR=_APPENGINEHTTPREQUEST,
        __module__="google.cloud.tasks_v2beta3.proto.target_pb2",
        __doc__="""App Engine HTTP request.
  
  The message defines the HTTP request that is sent to an App Engine app
  when the task is dispatched.
  
  This proto can only be used for tasks in a queue which has
  [app\_engine\_http\_queue][google.cloud.tasks.v2beta3.Queue.app\_engine\_http\_queue]
  set.
  
  Using
  [AppEngineHttpRequest][google.cloud.tasks.v2beta3.AppEngineHttpRequest]
  requires
  ```appengine.applications.get`` <https://cloud.google.com/appengine/docs/admin-api/access-control>`_
  Google IAM permission for the project and the following scope:
  
  ``https://www.googleapis.com/auth/cloud-platform``
  
  The task will be delivered to the App Engine app which belongs to the
  same project as the queue. For more information, see `How Requests are
  Routed <https://cloud.google.com/appengine/docs/standard/python/how-requests-are-routed>`_
  and how routing is affected by `dispatch
  files <https://cloud.google.com/appengine/docs/python/config/dispatchref>`_.
  
  The [AppEngineRouting][google.cloud.tasks.v2beta3.AppEngineRouting] used
  to construct the URL that the task is delivered to can be set at the
  queue-level or task-level:
  
  -  If set,
     [app\_engine\_routing\_override][google.cloud.tasks.v2beta3.AppEngineHttpQueue.app\_engine\_routing\_override]
     is used for all tasks in the queue, no matter what the setting is for
     the [task-level
     app\_engine\_routing][google.cloud.tasks.v2beta3.AppEngineHttpRequest.app\_engine\_routing].
  
  The ``url`` that the task will be sent to is:
  
  -  ``url =`` [host][google.cloud.tasks.v2beta3.AppEngineRouting.host]
     ``+``
     [relative\_uri][google.cloud.tasks.v2beta3.AppEngineHttpRequest.relative\_uri]
  
  The task attempt has succeeded if the app's request handler returns an
  HTTP response code in the range [``200`` - ``299``]. ``503`` is
  considered an App Engine system error instead of an application error.
  Requests returning error ``503`` will be retried regardless of retry
  configuration and not counted against retry counts. Any other response
  code or a failure to receive a response before the deadline is a failed
  attempt.
  
  
  Attributes:
      http_method:
          The HTTP method to use for the request. The default is POST.
          The app's request handler for the task's target URL must be
          able to handle HTTP requests with this http\_method, otherwise
          the task attempt will fail with error code 405 (Method Not
          Allowed). See `Writing a push task request handler <https://cl
          oud.google.com/appengine/docs/java/taskqueue/push/creating-
          handlers#writing_a_push_task_request_handler>`_ and the
          documentation for the request handlers in the language your
          app is written in e.g. `Python Request Handler <https://cloud.
          google.com/appengine/docs/python/tools/webapp/requesthandlercl
          ass>`_.
      app_engine_routing:
          Task-level setting for App Engine routing.  If set, [app\_engi
          ne\_routing\_override][google.cloud.tasks.v2beta3.AppEngineHtt
          pQueue.app\_engine\_routing\_override] is used for all tasks
          in the queue, no matter what the setting is for the [task-
          level app\_engine\_routing][google.cloud.tasks.v2beta3.AppEngi
          neHttpRequest.app\_engine\_routing].
      relative_uri:
          The relative URI.  The relative URI must begin with "/" and
          must be a valid HTTP relative URI. It can contain a path and
          query string arguments. If the relative URI is empty, then the
          root path "/" will be used. No spaces are allowed, and the
          maximum length allowed is 2083 characters.
      headers:
          HTTP request headers.  This map contains the header field
          names and values. Headers can be set when the [task is
          created][google.cloud.tasks.v2beta3.CloudTasks.CreateTask].
          Repeated headers are not supported but a header value can
          contain commas.  Cloud Tasks sets some headers to default
          values:  -  ``User-Agent``: By default, this header is
          ``"AppEngine-Google; (+http://code.google.com/appengine)"``.
          This    header can be modified, but Cloud Tasks will append
          ``"AppEngine-Google; (+http://code.google.com/appengine)"`` to
          the    modified ``User-Agent``.  If the task has a
          [body][google.cloud.tasks.v2beta3.AppEngineHttpRequest.body],
          Cloud Tasks sets the following headers:  -  ``Content-Type``:
          By default, the ``Content-Type`` header is set to
          ``"application/octet-stream"``. The default can be overridden
          by    explicitly setting ``Content-Type`` to a particular
          media type when    the [task is
          created][google.cloud.tasks.v2beta3.CloudTasks.CreateTask].
          For    example, ``Content-Type`` can be set to
          ``"application/json"``. -  ``Content-Length``: This is
          computed by Cloud Tasks. This value is    output only. It
          cannot be changed.  The headers below cannot be set or
          overridden:  -  ``Host`` -  ``X-Google-*`` -
          ``X-AppEngine-*``  In addition, Cloud Tasks sets some headers
          when the task is dispatched, such as headers containing
          information about the task; see `request headers <https://clou
          d.google.com/appengine/docs/python/taskqueue/push/creating-
          handlers#reading_request_headers>`_. These headers are set
          only when the task is dispatched, so they are not visible when
          the task is returned in a Cloud Tasks response.  Although
          there is no specific limit for the maximum number of headers
          or the size, there is a limit on the maximum size of the
          [Task][google.cloud.tasks.v2beta3.Task]. For more information,
          see the
          [CreateTask][google.cloud.tasks.v2beta3.CloudTasks.CreateTask]
          documentation.
      body:
          HTTP request body.  A request body is allowed only if the HTTP
          method is POST or PUT. It is an error to set a body on a task
          with an incompatible
          [HttpMethod][google.cloud.tasks.v2beta3.HttpMethod].
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.tasks.v2beta3.AppEngineHttpRequest)
    ),
)
_sym_db.RegisterMessage(AppEngineHttpRequest)
_sym_db.RegisterMessage(AppEngineHttpRequest.HeadersEntry)

AppEngineRouting = _reflection.GeneratedProtocolMessageType(
    "AppEngineRouting",
    (_message.Message,),
    dict(
        DESCRIPTOR=_APPENGINEROUTING,
        __module__="google.cloud.tasks_v2beta3.proto.target_pb2",
        __doc__="""App Engine Routing.
  
  Specifies the target URI. Since this target type dispatches tasks to
  secure app handlers, unsecure app handlers, and URIs restricted with
  ```login: admin`` <https://cloud.google.com/appengine/docs/standard/python/config/appref>`_
  the protocol (for example, HTTP or HTTPS) cannot be explictly specified.
  Task dispatches do not follow redirects and cannot target URI paths
  restricted with
  ```login: required`` <https://cloud.google.com/appengine/docs/standard/python/config/appref>`_
  because tasks are not run as any user.
  
  For more information about services, versions, and instances see `An
  Overview of App
  Engine <https://cloud.google.com/appengine/docs/python/an-overview-of-app-engine>`_,
  `Microservices Architecture on Google App
  Engine <https://cloud.google.com/appengine/docs/python/microservices-on-app-engine>`_,
  `App Engine Standard request
  routing <https://cloud.google.com/appengine/docs/standard/python/how-requests-are-routed>`_,
  and `App Engine Flex request
  routing <https://cloud.google.com/appengine/docs/flexible/python/how-requests-are-routed>`_.
  
  
  Attributes:
      service:
          App service.  By default, the task is sent to the service
          which is the default service when the task is attempted.  For
          some queues or tasks which were created using the App Engine
          Task Queue API,
          [host][google.cloud.tasks.v2beta3.AppEngineRouting.host] is
          not parsable into [service][google.cloud.tasks.v2beta3.AppEngi
          neRouting.service], [version][google.cloud.tasks.v2beta3.AppEn
          gineRouting.version], and [instance][google.cloud.tasks.v2beta
          3.AppEngineRouting.instance]. For example, some tasks which
          were created using the App Engine SDK use a custom domain
          name; custom domains are not parsed by Cloud Tasks. If
          [host][google.cloud.tasks.v2beta3.AppEngineRouting.host] is
          not parsable, then [service][google.cloud.tasks.v2beta3.AppEng
          ineRouting.service], [version][google.cloud.tasks.v2beta3.AppE
          ngineRouting.version], and [instance][google.cloud.tasks.v2bet
          a3.AppEngineRouting.instance] are the empty string.
      version:
          App version.  By default, the task is sent to the version
          which is the default version when the task is attempted.  For
          some queues or tasks which were created using the App Engine
          Task Queue API,
          [host][google.cloud.tasks.v2beta3.AppEngineRouting.host] is
          not parsable into [service][google.cloud.tasks.v2beta3.AppEngi
          neRouting.service], [version][google.cloud.tasks.v2beta3.AppEn
          gineRouting.version], and [instance][google.cloud.tasks.v2beta
          3.AppEngineRouting.instance]. For example, some tasks which
          were created using the App Engine SDK use a custom domain
          name; custom domains are not parsed by Cloud Tasks. If
          [host][google.cloud.tasks.v2beta3.AppEngineRouting.host] is
          not parsable, then [service][google.cloud.tasks.v2beta3.AppEng
          ineRouting.service], [version][google.cloud.tasks.v2beta3.AppE
          ngineRouting.version], and [instance][google.cloud.tasks.v2bet
          a3.AppEngineRouting.instance] are the empty string.
      instance:
          App instance.  By default, the task is sent to an instance
          which is available when the task is attempted.  Requests can
          only be sent to a specific instance if `manual scaling is used
          in App Engine Standard
          <https://cloud.google.com/appengine/docs/python/an-overview-
          of-app-engine?hl=en_US#scaling_types_and_instance_classes>`_.
          App Engine Flex does not support instances. For more
          information, see `App Engine Standard request routing
          <https://cloud.google.com/appengine/docs/standard/python/how-
          requests-are-routed>`_ and `App Engine Flex request routing
          <https://cloud.google.com/appengine/docs/flexible/python/how-
          requests-are-routed>`_.
      host:
          Output only. The host that the task is sent to.  The host is
          constructed from the domain name of the app associated with
          the queue's project ID (for example .appspot.com), and the [se
          rvice][google.cloud.tasks.v2beta3.AppEngineRouting.service], [
          version][google.cloud.tasks.v2beta3.AppEngineRouting.version],
          and [instance][google.cloud.tasks.v2beta3.AppEngineRouting.ins
          tance]. Tasks which were created using the App Engine SDK
          might have a custom domain name.  For more information, see
          `How Requests are Routed
          <https://cloud.google.com/appengine/docs/standard/python/how-
          requests-are-routed>`_.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.tasks.v2beta3.AppEngineRouting)
    ),
)
_sym_db.RegisterMessage(AppEngineRouting)


DESCRIPTOR._options = None
_APPENGINEHTTPREQUEST_HEADERSENTRY._options = None
# @@protoc_insertion_point(module_scope)
