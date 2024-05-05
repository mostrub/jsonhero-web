"""Generated client library for deploymentmanager version v2."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.generated_clients.apis.deploymentmanager.v2 import deploymentmanager_v2_messages as messages


class DeploymentmanagerV2(base_api.BaseApiClient):
  """Generated client library for service deploymentmanager version v2."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://deploymentmanager.googleapis.com/'
  MTLS_BASE_URL = 'https://deploymentmanager.mtls.googleapis.com/'

  _PACKAGE = 'deploymentmanager'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform', 'https://www.googleapis.com/auth/cloud-platform.read-only', 'https://www.googleapis.com/auth/ndev.cloudman', 'https://www.googleapis.com/auth/ndev.cloudman.readonly']
  _VERSION = 'v2'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'DeploymentmanagerV2'
  _URL_VERSION = 'v2'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new deploymentmanager handle."""
    url = url or self.BASE_URL
    super(DeploymentmanagerV2, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.deployments = self.DeploymentsService(self)
    self.manifests = self.ManifestsService(self)
    self.operations = self.OperationsService(self)
    self.resources = self.ResourcesService(self)
    self.types = self.TypesService(self)

  class DeploymentsService(base_api.BaseApiService):
    """Service class for the deployments resource."""

    _NAME = 'deployments'

    def __init__(self, client):
      super(DeploymentmanagerV2.DeploymentsService, self).__init__(client)
      self._upload_configs = {
          }

    def CancelPreview(self, request, global_params=None):
      r"""Cancels and removes the preview currently associated with the deployment.

      Args:
        request: (DeploymentmanagerDeploymentsCancelPreviewRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('CancelPreview')
      return self._RunMethod(
          config, request, global_params=global_params)

    CancelPreview.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='deploymentmanager.deployments.cancelPreview',
        ordered_params=['project', 'deployment'],
        path_params=['deployment', 'project'],
        query_params=[],
        relative_path='deploymentmanager/v2/projects/{project}/global/deployments/{deployment}/cancelPreview',
        request_field='deploymentsCancelPreviewRequest',
        request_type_name='DeploymentmanagerDeploymentsCancelPreviewRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a deployment and all of the resources in the deployment.

      Args:
        request: (DeploymentmanagerDeploymentsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        http_method='DELETE',
        method_id='deploymentmanager.deployments.delete',
        ordered_params=['project', 'deployment'],
        path_params=['deployment', 'project'],
        query_params=['deletePolicy'],
        relative_path='deploymentmanager/v2/projects/{project}/global/deployments/{deployment}',
        request_field='',
        request_type_name='DeploymentmanagerDeploymentsDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets information about a specific deployment.

      Args:
        request: (DeploymentmanagerDeploymentsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Deployment) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='deploymentmanager.deployments.get',
        ordered_params=['project', 'deployment'],
        path_params=['deployment', 'project'],
        query_params=[],
        relative_path='deploymentmanager/v2/projects/{project}/global/deployments/{deployment}',
        request_field='',
        request_type_name='DeploymentmanagerDeploymentsGetRequest',
        response_type_name='Deployment',
        supports_download=False,
    )

    def GetIamPolicy(self, request, global_params=None):
      r"""Gets the access control policy for a resource. May be empty if no such policy or resource exists.

      Args:
        request: (DeploymentmanagerDeploymentsGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='deploymentmanager.deployments.getIamPolicy',
        ordered_params=['project', 'resource'],
        path_params=['project', 'resource'],
        query_params=['optionsRequestedPolicyVersion'],
        relative_path='deploymentmanager/v2/projects/{project}/global/deployments/{resource}/getIamPolicy',
        request_field='',
        request_type_name='DeploymentmanagerDeploymentsGetIamPolicyRequest',
        response_type_name='Policy',
        supports_download=False,
    )

    def Insert(self, request, global_params=None):
      r"""Creates a deployment and all of the resources described by the deployment manifest.

      Args:
        request: (DeploymentmanagerDeploymentsInsertRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Insert')
      return self._RunMethod(
          config, request, global_params=global_params)

    Insert.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='deploymentmanager.deployments.insert',
        ordered_params=['project'],
        path_params=['project'],
        query_params=['createPolicy', 'preview'],
        relative_path='deploymentmanager/v2/projects/{project}/global/deployments',
        request_field='deployment',
        request_type_name='DeploymentmanagerDeploymentsInsertRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all deployments for a given project.

      Args:
        request: (DeploymentmanagerDeploymentsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (DeploymentsListResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='deploymentmanager.deployments.list',
        ordered_params=['project'],
        path_params=['project'],
        query_params=['filter', 'maxResults', 'orderBy', 'pageToken'],
        relative_path='deploymentmanager/v2/projects/{project}/global/deployments',
        request_field='',
        request_type_name='DeploymentmanagerDeploymentsListRequest',
        response_type_name='DeploymentsListResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Patches a deployment and all of the resources described by the deployment manifest.

      Args:
        request: (DeploymentmanagerDeploymentsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        http_method='PATCH',
        method_id='deploymentmanager.deployments.patch',
        ordered_params=['project', 'deployment'],
        path_params=['deployment', 'project'],
        query_params=['createPolicy', 'deletePolicy', 'preview'],
        relative_path='deploymentmanager/v2/projects/{project}/global/deployments/{deployment}',
        request_field='deploymentResource',
        request_type_name='DeploymentmanagerDeploymentsPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def SetIamPolicy(self, request, global_params=None):
      r"""Sets the access control policy on the specified resource. Replaces any existing policy.

      Args:
        request: (DeploymentmanagerDeploymentsSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='deploymentmanager.deployments.setIamPolicy',
        ordered_params=['project', 'resource'],
        path_params=['project', 'resource'],
        query_params=[],
        relative_path='deploymentmanager/v2/projects/{project}/global/deployments/{resource}/setIamPolicy',
        request_field='globalSetPolicyRequest',
        request_type_name='DeploymentmanagerDeploymentsSetIamPolicyRequest',
        response_type_name='Policy',
        supports_download=False,
    )

    def Stop(self, request, global_params=None):
      r"""Stops an ongoing operation. This does not roll back any work that has already been completed, but prevents any new work from being started.

      Args:
        request: (DeploymentmanagerDeploymentsStopRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Stop')
      return self._RunMethod(
          config, request, global_params=global_params)

    Stop.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='deploymentmanager.deployments.stop',
        ordered_params=['project', 'deployment'],
        path_params=['deployment', 'project'],
        query_params=[],
        relative_path='deploymentmanager/v2/projects/{project}/global/deployments/{deployment}/stop',
        request_field='deploymentsStopRequest',
        request_type_name='DeploymentmanagerDeploymentsStopRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      r"""Returns permissions that a caller has on the specified resource.

      Args:
        request: (DeploymentmanagerDeploymentsTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestIamPermissions.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='deploymentmanager.deployments.testIamPermissions',
        ordered_params=['project', 'resource'],
        path_params=['project', 'resource'],
        query_params=[],
        relative_path='deploymentmanager/v2/projects/{project}/global/deployments/{resource}/testIamPermissions',
        request_field='testPermissionsRequest',
        request_type_name='DeploymentmanagerDeploymentsTestIamPermissionsRequest',
        response_type_name='TestPermissionsResponse',
        supports_download=False,
    )

    def Update(self, request, global_params=None):
      r"""Updates a deployment and all of the resources described by the deployment manifest.

      Args:
        request: (DeploymentmanagerDeploymentsUpdateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

    Update.method_config = lambda: base_api.ApiMethodInfo(
        http_method='PUT',
        method_id='deploymentmanager.deployments.update',
        ordered_params=['project', 'deployment'],
        path_params=['deployment', 'project'],
        query_params=['createPolicy', 'deletePolicy', 'preview'],
        relative_path='deploymentmanager/v2/projects/{project}/global/deployments/{deployment}',
        request_field='deploymentResource',
        request_type_name='DeploymentmanagerDeploymentsUpdateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ManifestsService(base_api.BaseApiService):
    """Service class for the manifests resource."""

    _NAME = 'manifests'

    def __init__(self, client):
      super(DeploymentmanagerV2.ManifestsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets information about a specific manifest.

      Args:
        request: (DeploymentmanagerManifestsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Manifest) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='deploymentmanager.manifests.get',
        ordered_params=['project', 'deployment', 'manifest'],
        path_params=['deployment', 'manifest', 'project'],
        query_params=[],
        relative_path='deploymentmanager/v2/projects/{project}/global/deployments/{deployment}/manifests/{manifest}',
        request_field='',
        request_type_name='DeploymentmanagerManifestsGetRequest',
        response_type_name='Manifest',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all manifests for a given deployment.

      Args:
        request: (DeploymentmanagerManifestsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ManifestsListResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='deploymentmanager.manifests.list',
        ordered_params=['project', 'deployment'],
        path_params=['deployment', 'project'],
        query_params=['filter', 'maxResults', 'orderBy', 'pageToken'],
        relative_path='deploymentmanager/v2/projects/{project}/global/deployments/{deployment}/manifests',
        request_field='',
        request_type_name='DeploymentmanagerManifestsListRequest',
        response_type_name='ManifestsListResponse',
        supports_download=False,
    )

  class OperationsService(base_api.BaseApiService):
    """Service class for the operations resource."""

    _NAME = 'operations'

    def __init__(self, client):
      super(DeploymentmanagerV2.OperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets information about a specific operation.

      Args:
        request: (DeploymentmanagerOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='deploymentmanager.operations.get',
        ordered_params=['project', 'operation'],
        path_params=['operation', 'project'],
        query_params=[],
        relative_path='deploymentmanager/v2/projects/{project}/global/operations/{operation}',
        request_field='',
        request_type_name='DeploymentmanagerOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all operations for a project.

      Args:
        request: (DeploymentmanagerOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (OperationsListResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='deploymentmanager.operations.list',
        ordered_params=['project'],
        path_params=['project'],
        query_params=['filter', 'maxResults', 'orderBy', 'pageToken'],
        relative_path='deploymentmanager/v2/projects/{project}/global/operations',
        request_field='',
        request_type_name='DeploymentmanagerOperationsListRequest',
        response_type_name='OperationsListResponse',
        supports_download=False,
    )

  class ResourcesService(base_api.BaseApiService):
    """Service class for the resources resource."""

    _NAME = 'resources'

    def __init__(self, client):
      super(DeploymentmanagerV2.ResourcesService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets information about a single resource.

      Args:
        request: (DeploymentmanagerResourcesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Resource) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='deploymentmanager.resources.get',
        ordered_params=['project', 'deployment', 'resource'],
        path_params=['deployment', 'project', 'resource'],
        query_params=[],
        relative_path='deploymentmanager/v2/projects/{project}/global/deployments/{deployment}/resources/{resource}',
        request_field='',
        request_type_name='DeploymentmanagerResourcesGetRequest',
        response_type_name='Resource',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all resources in a given deployment.

      Args:
        request: (DeploymentmanagerResourcesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ResourcesListResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='deploymentmanager.resources.list',
        ordered_params=['project', 'deployment'],
        path_params=['deployment', 'project'],
        query_params=['filter', 'maxResults', 'orderBy', 'pageToken'],
        relative_path='deploymentmanager/v2/projects/{project}/global/deployments/{deployment}/resources',
        request_field='',
        request_type_name='DeploymentmanagerResourcesListRequest',
        response_type_name='ResourcesListResponse',
        supports_download=False,
    )

  class TypesService(base_api.BaseApiService):
    """Service class for the types resource."""

    _NAME = 'types'

    def __init__(self, client):
      super(DeploymentmanagerV2.TypesService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      r"""Lists all resource types for Deployment Manager.

      Args:
        request: (DeploymentmanagerTypesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TypesListResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='deploymentmanager.types.list',
        ordered_params=['project'],
        path_params=['project'],
        query_params=['filter', 'maxResults', 'orderBy', 'pageToken'],
        relative_path='deploymentmanager/v2/projects/{project}/global/types',
        request_field='',
        request_type_name='DeploymentmanagerTypesListRequest',
        response_type_name='TypesListResponse',
        supports_download=False,
    )