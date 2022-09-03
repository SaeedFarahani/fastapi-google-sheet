# USERSApi

All URIs are relative to **

Method | HTTP request | Description
------------- | ------------- | -------------
[**addUserASSIGNMENTApiV1UserAddPost**](USERSApi.md#addUserASSIGNMENTApiV1UserAddPost) | **POST** /ASSIGNMENT/api/v1/user/add | Add User
[**deleteUserASSIGNMENTApiV1UserDeleteIdDelete**](USERSApi.md#deleteUserASSIGNMENTApiV1UserDeleteIdDelete) | **DELETE** /ASSIGNMENT/api/v1/user/delete/{id} | Delete User
[**getUserASSIGNMENTApiV1UserGetGet**](USERSApi.md#getUserASSIGNMENTApiV1UserGetGet) | **GET** /ASSIGNMENT/api/v1/user/get | Get User
[**loginASSIGNMENTApiV1UsersLoginPost**](USERSApi.md#loginASSIGNMENTApiV1UsersLoginPost) | **POST** /ASSIGNMENT/api/v1/users/login | Login
[**refreshASSIGNMENTApiV1UsersRefreshPost**](USERSApi.md#refreshASSIGNMENTApiV1UsersRefreshPost) | **POST** /ASSIGNMENT/api/v1/users/refresh | Refresh
[**updateUserASSIGNMENTApiV1UserUpdateIdPut**](USERSApi.md#updateUserASSIGNMENTApiV1UserUpdateIdPut) | **PUT** /ASSIGNMENT/api/v1/user/update/{id} | Update User



## addUserASSIGNMENTApiV1UserAddPost

Add User

### Example

```bash
 addUserASSIGNMENTApiV1UserAddPost
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **age** | **string** |  | [default to null]
 **file** | **binary** |  | [default to null]
 **nid** | **string** |  | [default to null]
 **username** | **string** |  | [default to null]
 **firstname** | **string** |  | [optional] [default to ]
 **lastname** | **string** |  | [optional] [default to ]

### Return type

[**VmResponseBase**](VmResponseBase.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## deleteUserASSIGNMENTApiV1UserDeleteIdDelete

Delete User

### Example

```bash
 deleteUserASSIGNMENTApiV1UserDeleteIdDelete id=value
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**AnyType**](.md) |  | [default to null]

### Return type

[**VmResponseBase**](VmResponseBase.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not Applicable
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## getUserASSIGNMENTApiV1UserGetGet

Get User

### Example

```bash
 getUserASSIGNMENTApiV1UserGetGet  skip=value  limit=value
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **integer** |  | [optional] [default to 0]
 **limit** | **integer** |  | [optional] [default to 1000]

### Return type

[**array[Users]**](Users.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not Applicable
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## loginASSIGNMENTApiV1UsersLoginPost

Login

### Example

```bash
 loginASSIGNMENTApiV1UsersLoginPost
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vmUp** | [**VmUp**](VmUp.md) |  |

### Return type

[**VmResponse**](VmResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## refreshASSIGNMENTApiV1UsersRefreshPost

Refresh

The jwt_refresh_token_required() function insures a valid refresh
token is present in the request before running any code below that function.
we can use the get_jwt_subject() function to get the subject of the refresh
token, and use the create_access_token() function again to make a new access token

### Example

```bash
 refreshASSIGNMENTApiV1UsersRefreshPost
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**VmResponse**](VmResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not Applicable
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## updateUserASSIGNMENTApiV1UserUpdateIdPut

Update User

### Example

```bash
 updateUserASSIGNMENTApiV1UserUpdateIdPut id=value
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**AnyType**](.md) |  | [default to null]
 **age** | **string** |  | [default to null]
 **file** | **binary** |  | [default to null]
 **nid** | **string** |  | [default to null]
 **username** | **string** |  | [default to null]
 **firstname** | **string** |  | [optional] [default to ]
 **lastname** | **string** |  | [optional] [default to ]

### Return type

[**VmResponseBase**](VmResponseBase.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

