# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import cast, List, TYPE_CHECKING

import six

from azure.core.tracing.decorator import distributed_trace
from ._generated import SearchIndexClient
from ._generated.models import IndexBatch, IndexingResult
from ._index_documents_batch import IndexDocumentsBatch
from ._paging import SearchItemPaged, SearchPageIterator
from ._queries import AutocompleteQuery, SearchQuery, SuggestQuery
from .._headers_mixin import HeadersMixin
from .._version import SDK_MONIKER

if TYPE_CHECKING:
    # pylint:disable=unused-import,ungrouped-imports
    from typing import Any, Union
    from azure.core.credentials import AzureKeyCredential


def odata(statement, **kwargs):
    """Escape an OData query string.

    The statement to prepare should include fields to substitute given inside
    braces, e.g. `{somevar}` and then pass the corresponing value as a keyword
    argument, e.g. `somevar=10`.

    :param statement: An OData query string to prepare
    :type statement: str
    :rtype: str

    .. admonition:: Example:

        >>> odata("name eq {name} and age eq {age}", name="O'Neil", age=37)
        "name eq 'O''Neil' and age eq 37"


    """
    kw = dict(kwargs)
    for key in kw:
        value = kw[key]
        if isinstance(value, six.string_types):
            value = value.replace("'", "''")
            if "'{{{}}}'".format(key) not in statement:
                kw[key] = "'{}'".format(value)
    return statement.format(**kw)


class SearchClient(HeadersMixin):
    """A client to interact with an existing Azure search index.

    :param endpoint: The URL endpoint of an Azure search service
    :type endpoint: str
    :param index_name: The name of the index to connect to
    :type index_name: str
    :param credential: A credential to authorize search client requests
    :type credential: ~azure.core.credentials.AzureKeyCredential

    .. admonition:: Example:

        .. literalinclude:: ../samples/sample_authentication.py
            :start-after: [START create_search_client_with_key]
            :end-before: [END create_search_client_with_key]
            :language: python
            :dedent: 4
            :caption: Creating the SearchClient with an API key.
    """

    _ODATA_ACCEPT = "application/json;odata.metadata=none"  # type: str

    def __init__(self, endpoint, index_name, credential, **kwargs):
        # type: (str, str, AzureKeyCredential, **Any) -> None

        self._endpoint = endpoint  # type: str
        self._index_name = index_name  # type: str
        self._credential = credential  # type: AzureKeyCredential
        self._client = SearchIndexClient(
            endpoint=endpoint, index_name=index_name, sdk_moniker=SDK_MONIKER, **kwargs
        )  # type: SearchIndexClient

    def __repr__(self):
        # type: () -> str
        return "<SearchClient [endpoint={}, index={}]>".format(
            repr(self._endpoint), repr(self._index_name)
        )[:1024]

    def close(self):
        # type: () -> None
        """Close the :class:`~azure.search.SearchClient` session.

        """
        return self._client.close()

    @distributed_trace
    def get_document_count(self, **kwargs):
        # type: (**Any) -> int
        """Return the number of documents in the Azure search index.

        :rtype: int
        """
        kwargs["headers"] = self._merge_client_headers(kwargs.get("headers"))
        return int(self._client.documents.count(**kwargs))

    @distributed_trace
    def get_document(self, key, selected_fields=None, **kwargs):
        # type: (str, List[str], **Any) -> dict
        """Retrieve a document from the Azure search index by its key.

        :param key: The primary key value for the document to retrieve
        :type key: str
        :param selected_fields: a whitelist of fields to include in the results
        :type selected_fields: List[str]
        :rtype:  dict

        .. admonition:: Example:

            .. literalinclude:: ../samples/sample_get_document.py
                :start-after: [START get_document]
                :end-before: [END get_document]
                :language: python
                :dedent: 4
                :caption: Get a specific document from the search index.
        """
        kwargs["headers"] = self._merge_client_headers(kwargs.get("headers"))
        result = self._client.documents.get(
            key=key, selected_fields=selected_fields, **kwargs
        )
        return cast(dict, result)

    @distributed_trace
    def search(self, search_text, **kwargs):
        # type: (str, **Any) -> SearchItemPaged[dict]
        """Search the Azure search index for documents.

        :param str search_text: A full-text search query expression; Use "*" or omit this parameter to
        match all documents.
        :rtype:  SearchItemPaged[dict]

        .. admonition:: Example:

            .. literalinclude:: ../samples/sample_simple_query.py
                :start-after: [START simple_query]
                :end-before: [END simple_query]
                :language: python
                :dedent: 4
                :caption: Search on a simple text term.

        .. admonition:: Example:

            .. literalinclude:: ../samples/sample_filter_query.py
                :start-after: [START filter_query]
                :end-before: [END filter_query]
                :language: python
                :dedent: 4
                :caption: Filter and sort search results.

        .. admonition:: Example:

            .. literalinclude:: ../samples/sample_facet_query.py
                :start-after: [START facet_query]
                :end-before: [END facet_query]
                :language: python
                :dedent: 4
                :caption: Get search result facets.
        """
        include_total_result_count = kwargs.pop("include_total_result_count", None)
        facets = kwargs.pop("facets", None)
        filter_arg = kwargs.pop("filter", None)
        highlight_fields = kwargs.pop("highlight_fields", None)
        highlight_post_tag = kwargs.pop("highlight_post_tag", None)
        highlight_pre_tag = kwargs.pop("highlight_pre_tag", None)
        minimum_coverage = kwargs.pop("minimum_coverage", None)
        order_by = kwargs.pop("order_by", None)
        query_type = kwargs.pop("query_type", None)
        scoring_parameters = kwargs.pop("scoring_parameters", None)
        scoring_profile = kwargs.pop("scoring_profile", None)
        search_fields = kwargs.pop("search_fields", None)
        search_mode = kwargs.pop("search_mode", None)
        select = kwargs.pop("select", None)
        skip = kwargs.pop("skip", None)
        top = kwargs.pop("top", None)
        query = SearchQuery(
            search_text=search_text,
            include_total_result_count=include_total_result_count,
            facets=facets,
            filter=filter_arg,
            highlight_fields=highlight_fields,
            highlight_post_tag=highlight_post_tag,
            highlight_pre_tag=highlight_pre_tag,
            minimum_coverage=minimum_coverage,
            order_by=order_by,
            query_type=query_type,
            scoring_parameters=scoring_parameters,
            scoring_profile=scoring_profile,
            search_fields=search_fields,
            search_mode=search_mode,
            select=select,
            skip=skip,
            top=top
        )

        kwargs["headers"] = self._merge_client_headers(kwargs.get("headers"))
        return SearchItemPaged(
            self._client, query, kwargs, page_iterator_class=SearchPageIterator
        )

    @distributed_trace
    def suggest(self, search_text, suggester_name, **kwargs):
        # type: (str, str, **Any) -> List[dict]
        """Get search suggestion results from the Azure search index.

        :param str search_text: Required. The search text to use to suggest documents. Must be at least 1
        character, and no more than 100 characters.
        :param str suggester_name: Required. The name of the suggester as specified in the suggesters
        collection that's part of the index definition.
        :rtype:  List[dict]

        .. admonition:: Example:

            .. literalinclude:: ../samples/sample_suggestions.py
                :start-after: [START suggest_query]
                :end-before: [END suggest_query]
                :language: python
                :dedent: 4
                :caption: Get search suggestions.
        """
        filter_arg = kwargs.pop("filter", None)
        use_fuzzy_matching = kwargs.pop("use_fuzzy_matching", None)
        highlight_post_tag = kwargs.pop("highlight_post_tag", None)
        highlight_pre_tag = kwargs.pop("highlight_pre_tag", None)
        minimum_coverage = kwargs.pop("minimum_coverage", None)
        order_by = kwargs.pop("order_by", None)
        search_fields = kwargs.pop("search_fields", None)
        select = kwargs.pop("select", None)
        top = kwargs.pop("top", None)
        query = SuggestQuery(
            search_text=search_text,
            suggester_name=suggester_name,
            filter=filter_arg,
            use_fuzzy_matching=use_fuzzy_matching,
            highlight_post_tag=highlight_post_tag,
            highlight_pre_tag=highlight_pre_tag,
            minimum_coverage=minimum_coverage,
            order_by=order_by,
            search_fields=search_fields,
            select=select,
            top=top
        )

        kwargs["headers"] = self._merge_client_headers(kwargs.get("headers"))
        response = self._client.documents.suggest_post(
            suggest_request=query.request, **kwargs
        )
        results = [r.as_dict() for r in response.results]
        return results

    @distributed_trace
    def autocomplete(self, search_text, suggester_name, **kwargs):
        # type: (str, str, **Any) -> List[dict]
        """Get search auto-completion results from the Azure search index.

        :param str search_text: The search text on which to base autocomplete results.
        :param str suggester_name: The name of the suggester as specified in the suggesters
        collection that's part of the index definition.
        :rtype:  List[dict]

        .. admonition:: Example:

            .. literalinclude:: ../samples/sample_autocomplete.py
                :start-after: [START autocomplete_query]
                :end-before: [END autocomplete_query]
                :language: python
                :dedent: 4
                :caption: Get a auto-completions.
        """
        autocomplete_mode = kwargs.pop("autocomplete_mode", None)
        filter_arg = kwargs.pop("filter", None)
        use_fuzzy_matching = kwargs.pop("use_fuzzy_matching", None)
        highlight_post_tag = kwargs.pop("highlight_post_tag", None)
        highlight_pre_tag = kwargs.pop("highlight_pre_tag", None)
        minimum_coverage = kwargs.pop("minimum_coverage", None)
        search_fields = kwargs.pop("search_fields", None)
        top = kwargs.pop("top", None)
        query = AutocompleteQuery(
            search_text=search_text,
            suggester_name=suggester_name,
            autocomplete_mode=autocomplete_mode,
            filter=filter_arg,
            use_fuzzy_matching=use_fuzzy_matching,
            highlight_post_tag=highlight_post_tag,
            highlight_pre_tag=highlight_pre_tag,
            minimum_coverage=minimum_coverage,
            search_fields=search_fields,
            top=top
        )

        kwargs["headers"] = self._merge_client_headers(kwargs.get("headers"))
        response = self._client.documents.autocomplete_post(
            autocomplete_request=query.request, **kwargs
        )
        results = [r.as_dict() for r in response.results]
        return results

    def upload_documents(self, documents, **kwargs):
        # type: (List[dict], **Any) -> List[IndexingResult]
        """Upload documents to the Azure search index.

        An upload action is similar to an "upsert" where the document will be
        inserted if it is new and updated/replaced if it exists. All fields are
        replaced in the update case.

        :param documents: A list of documents to upload.
        :type documents: List[dict]
        :rtype:  List[IndexingResult]

        .. admonition:: Example:

            .. literalinclude:: ../samples/sample_crud_operations.py
                :start-after: [START upload_document]
                :end-before: [END upload_document]
                :language: python
                :dedent: 4
                :caption: Upload new documents to an index
        """
        batch = IndexDocumentsBatch()
        batch.add_upload_actions(documents)

        kwargs["headers"] = self._merge_client_headers(kwargs.get("headers"))
        results = self.index_documents(batch, **kwargs)
        return cast(List[IndexingResult], results)

    def delete_documents(self, documents, **kwargs):
        # type: (List[dict], **Any) -> List[IndexingResult]
        """Delete documents from the Azure search index

        Delete removes the specified document from the index. Any field you
        specify in a delete operation, other than the key field, will be
        ignored. If you want to remove an individual field from a document, use
        `merge_documents` instead and set the field explicitly to None.

        Delete operations are idempotent. That is, even if a document key does
        not exist in the index, attempting a delete operation with that key will
        result in a 200 status code.

        :param documents: A list of documents to delete.
        :type documents: List[dict]
        :rtype:  List[IndexingResult]

        .. admonition:: Example:

            .. literalinclude:: ../samples/sample_crud_operations.py
                :start-after: [START delete_document]
                :end-before: [END delete_document]
                :language: python
                :dedent: 4
                :caption: Delete existing documents to an index
        """
        batch = IndexDocumentsBatch()
        batch.add_delete_actions(documents)

        kwargs["headers"] = self._merge_client_headers(kwargs.get("headers"))
        results = self.index_documents(batch, **kwargs)
        return cast(List[IndexingResult], results)

    def merge_documents(self, documents, **kwargs):
        # type: (List[dict], **Any) -> List[IndexingResult]
        """Merge documents in to existing documents in the Azure search index.

        Merge updates an existing document with the specified fields. If the
        document doesn't exist, the merge will fail. Any field you specify in a
        merge will replace the existing field in the document. This also applies
        to collections of primitive and complex types.

        :param documents: A list of documents to merge.
        :type documents: List[dict]
        :rtype:  List[IndexingResult]

        .. admonition:: Example:

            .. literalinclude:: ../samples/sample_crud_operations.py
                :start-after: [START merge_document]
                :end-before: [END merge_document]
                :language: python
                :dedent: 4
                :caption: Merge fields into existing documents to an index
        """
        batch = IndexDocumentsBatch()
        batch.add_merge_actions(documents)

        kwargs["headers"] = self._merge_client_headers(kwargs.get("headers"))
        results = self.index_documents(batch, **kwargs)
        return cast(List[IndexingResult], results)

    def merge_or_upload_documents(self, documents, **kwargs):
        # type: (List[dict], **Any) -> List[IndexingResult]
        """Merge documents in to existing documents in the Azure search index,
        or upload them if they do not yet exist.

        This action behaves like `merge_documents` if a document with the given
        key already exists in the index. If the document does not exist, it
        behaves like `upload_documents` with a new document.

        :param documents: A list of documents to merge or upload.
        :type documents: List[dict]
        :rtype:  List[IndexingResult]
        """
        batch = IndexDocumentsBatch()
        batch.add_merge_or_upload_actions(documents)

        kwargs["headers"] = self._merge_client_headers(kwargs.get("headers"))
        results = self.index_documents(batch, **kwargs)
        return cast(List[IndexingResult], results)

    @distributed_trace
    def index_documents(self, batch, **kwargs):
        # type: (IndexDocumentsBatch, **Any) -> List[IndexingResult]
        """Specify a document operations to perform as a batch.

        :param batch: A batch of document operations to perform.
        :type batch: IndexDocumentsBatch
        :rtype:  List[IndexingResult]
        """
        index_documents = IndexBatch(actions=batch.actions)

        kwargs["headers"] = self._merge_client_headers(kwargs.get("headers"))
        batch_response = self._client.documents.index(batch=index_documents, **kwargs)
        return cast(List[IndexingResult], batch_response.results)

    def __enter__(self):
        # type: () -> SearchClient
        self._client.__enter__()  # pylint:disable=no-member
        return self

    def __exit__(self, *args):
        # type: (*Any) -> None
        self._client.__exit__(*args)  # pylint:disable=no-member
