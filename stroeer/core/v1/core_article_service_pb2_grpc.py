# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from stroeer.core.v1 import article_pb2 as stroeer_dot_core_dot_v1_dot_article__pb2
from stroeer.core.v1 import core_article_service_pb2 as stroeer_dot_core_dot_v1_dot_core__article__service__pb2


class ArticleServiceStub(object):
    """*
    ```protobuf
    service ArticleService {
    // get a single article by its `article_id`
    rpc GetArticle (GetArticleRequest) returns (stroeer.core.v1.Article) {}
    // similar to GetArticle(), but retrieves multiple items at once (max == 100)
    rpc BatchGetArticles (BatchArticlesRequest) returns (BatchArticlesResponse) {}
    // query multiple articles at once
    rpc ListArticles (ListArticlesRequest) returns (ListArticlesResponse) {}
    // list the available root sections
    rpc ListSections (google.protobuf.Empty) returns (ListSectionsResponse) {}
    }
    ```
    Core service to either query a single article (`rpc GetArticle()`) identified
    by its id or to query multiple articles (`rpc ListArticles()`) by providing
    a query.

    All results returned from this service are _unfiltered_, hence they may contain
    [`elements`](element.html) that are *expired*, *not yet valid* or whose [`state`](metadata.html#state)
    is not `PUBLISHED`.

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetArticle = channel.unary_unary(
                '/stroeer.core.v1.ArticleService/GetArticle',
                request_serializer=stroeer_dot_core_dot_v1_dot_core__article__service__pb2.GetArticleRequest.SerializeToString,
                response_deserializer=stroeer_dot_core_dot_v1_dot_article__pb2.Article.FromString,
                )
        self.BatchGetArticles = channel.unary_unary(
                '/stroeer.core.v1.ArticleService/BatchGetArticles',
                request_serializer=stroeer_dot_core_dot_v1_dot_core__article__service__pb2.BatchGetArticlesRequest.SerializeToString,
                response_deserializer=stroeer_dot_core_dot_v1_dot_core__article__service__pb2.BatchGetArticlesResponse.FromString,
                )
        self.ListArticles = channel.unary_unary(
                '/stroeer.core.v1.ArticleService/ListArticles',
                request_serializer=stroeer_dot_core_dot_v1_dot_core__article__service__pb2.ListArticlesRequest.SerializeToString,
                response_deserializer=stroeer_dot_core_dot_v1_dot_core__article__service__pb2.ListArticlesResponse.FromString,
                )
        self.ListSections = channel.unary_unary(
                '/stroeer.core.v1.ArticleService/ListSections',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=stroeer_dot_core_dot_v1_dot_core__article__service__pb2.ListSectionsResponse.FromString,
                )


class ArticleServiceServicer(object):
    """*
    ```protobuf
    service ArticleService {
    // get a single article by its `article_id`
    rpc GetArticle (GetArticleRequest) returns (stroeer.core.v1.Article) {}
    // similar to GetArticle(), but retrieves multiple items at once (max == 100)
    rpc BatchGetArticles (BatchArticlesRequest) returns (BatchArticlesResponse) {}
    // query multiple articles at once
    rpc ListArticles (ListArticlesRequest) returns (ListArticlesResponse) {}
    // list the available root sections
    rpc ListSections (google.protobuf.Empty) returns (ListSectionsResponse) {}
    }
    ```
    Core service to either query a single article (`rpc GetArticle()`) identified
    by its id or to query multiple articles (`rpc ListArticles()`) by providing
    a query.

    All results returned from this service are _unfiltered_, hence they may contain
    [`elements`](element.html) that are *expired*, *not yet valid* or whose [`state`](metadata.html#state)
    is not `PUBLISHED`.

    """

    def GetArticle(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchGetArticles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListArticles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListSections(self, request, context):
        """Allow Empty as request param
        buf:lint:ignore RPC_REQUEST_STANDARD_NAME
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ArticleServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetArticle': grpc.unary_unary_rpc_method_handler(
                    servicer.GetArticle,
                    request_deserializer=stroeer_dot_core_dot_v1_dot_core__article__service__pb2.GetArticleRequest.FromString,
                    response_serializer=stroeer_dot_core_dot_v1_dot_article__pb2.Article.SerializeToString,
            ),
            'BatchGetArticles': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchGetArticles,
                    request_deserializer=stroeer_dot_core_dot_v1_dot_core__article__service__pb2.BatchGetArticlesRequest.FromString,
                    response_serializer=stroeer_dot_core_dot_v1_dot_core__article__service__pb2.BatchGetArticlesResponse.SerializeToString,
            ),
            'ListArticles': grpc.unary_unary_rpc_method_handler(
                    servicer.ListArticles,
                    request_deserializer=stroeer_dot_core_dot_v1_dot_core__article__service__pb2.ListArticlesRequest.FromString,
                    response_serializer=stroeer_dot_core_dot_v1_dot_core__article__service__pb2.ListArticlesResponse.SerializeToString,
            ),
            'ListSections': grpc.unary_unary_rpc_method_handler(
                    servicer.ListSections,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=stroeer_dot_core_dot_v1_dot_core__article__service__pb2.ListSectionsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'stroeer.core.v1.ArticleService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ArticleService(object):
    """*
    ```protobuf
    service ArticleService {
    // get a single article by its `article_id`
    rpc GetArticle (GetArticleRequest) returns (stroeer.core.v1.Article) {}
    // similar to GetArticle(), but retrieves multiple items at once (max == 100)
    rpc BatchGetArticles (BatchArticlesRequest) returns (BatchArticlesResponse) {}
    // query multiple articles at once
    rpc ListArticles (ListArticlesRequest) returns (ListArticlesResponse) {}
    // list the available root sections
    rpc ListSections (google.protobuf.Empty) returns (ListSectionsResponse) {}
    }
    ```
    Core service to either query a single article (`rpc GetArticle()`) identified
    by its id or to query multiple articles (`rpc ListArticles()`) by providing
    a query.

    All results returned from this service are _unfiltered_, hence they may contain
    [`elements`](element.html) that are *expired*, *not yet valid* or whose [`state`](metadata.html#state)
    is not `PUBLISHED`.

    """

    @staticmethod
    def GetArticle(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/stroeer.core.v1.ArticleService/GetArticle',
            stroeer_dot_core_dot_v1_dot_core__article__service__pb2.GetArticleRequest.SerializeToString,
            stroeer_dot_core_dot_v1_dot_article__pb2.Article.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BatchGetArticles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/stroeer.core.v1.ArticleService/BatchGetArticles',
            stroeer_dot_core_dot_v1_dot_core__article__service__pb2.BatchGetArticlesRequest.SerializeToString,
            stroeer_dot_core_dot_v1_dot_core__article__service__pb2.BatchGetArticlesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListArticles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/stroeer.core.v1.ArticleService/ListArticles',
            stroeer_dot_core_dot_v1_dot_core__article__service__pb2.ListArticlesRequest.SerializeToString,
            stroeer_dot_core_dot_v1_dot_core__article__service__pb2.ListArticlesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListSections(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/stroeer.core.v1.ArticleService/ListSections',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            stroeer_dot_core_dot_v1_dot_core__article__service__pb2.ListSectionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
