# DEEPLEARNINGApi

All URIs are relative to **

Method | HTTP request | Description
------------- | ------------- | -------------
[**loadAndTestModelByIndexASSIGNMENTApiV1LoadAndTestModelByIndexGet**](DEEPLEARNINGApi.md#loadAndTestModelByIndexASSIGNMENTApiV1LoadAndTestModelByIndexGet) | **GET** /ASSIGNMENT/api/v1/load-and-test-model-by-index | Load And Test Model By Index
[**loadAndTestModelASSIGNMENTApiV1LoadAndTestModelGet**](DEEPLEARNINGApi.md#loadAndTestModelASSIGNMENTApiV1LoadAndTestModelGet) | **GET** /ASSIGNMENT/api/v1/load-and-test-model | Load And Test Model
[**testAccuracyForRangeOfDataASSIGNMENTApiV1TestAccuracyForRangeOfDataGet**](DEEPLEARNINGApi.md#testAccuracyForRangeOfDataASSIGNMENTApiV1TestAccuracyForRangeOfDataGet) | **GET** /ASSIGNMENT/api/v1/test-accuracy-for-range-of-data | Test Accuracy For Range Of Data
[**trainAndSaveModelASSIGNMENTApiV1TrainAndSaveModelGet**](DEEPLEARNINGApi.md#trainAndSaveModelASSIGNMENTApiV1TrainAndSaveModelGet) | **GET** /ASSIGNMENT/api/v1/train-and-save-model | Train And Save Model



## loadAndTestModelByIndexASSIGNMENTApiV1LoadAndTestModelByIndexGet

Load And Test Model By Index

### Example

```bash
 loadAndTestModelByIndexASSIGNMENTApiV1LoadAndTestModelByIndexGet  index=value
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **integer** |  | [default to null]

### Return type

[**AnyType**](AnyType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not Applicable
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## loadAndTestModelASSIGNMENTApiV1LoadAndTestModelGet

Load And Test Model

### Example

```bash
 loadAndTestModelASSIGNMENTApiV1LoadAndTestModelGet  my_image=value
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **myImage** | **string** |  | [default to null]

### Return type

[**AnyType**](AnyType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not Applicable
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## testAccuracyForRangeOfDataASSIGNMENTApiV1TestAccuracyForRangeOfDataGet

Test Accuracy For Range Of Data

### Example

```bash
 testAccuracyForRangeOfDataASSIGNMENTApiV1TestAccuracyForRangeOfDataGet  idx1=value  idx2=value
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idx1** | **integer** |  | [default to null]
 **idx2** | **integer** |  | [default to null]

### Return type

[**AnyType**](AnyType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not Applicable
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## trainAndSaveModelASSIGNMENTApiV1TrainAndSaveModelGet

Train And Save Model

### Example

```bash
 trainAndSaveModelASSIGNMENTApiV1TrainAndSaveModelGet  num_iterations=value  learning_rate=value  print_cost=value
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **numIterations** | **integer** |  | [optional] [default to 2000]
 **learningRate** | **integer** |  | [optional] [default to 0.005]
 **printCost** | **boolean** |  | [optional] [default to true]

### Return type

[**AnyType**](AnyType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not Applicable
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

