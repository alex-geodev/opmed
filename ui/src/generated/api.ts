/* tslint:disable */
/* eslint-disable */
/**
 * Stitched Up
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


import type { Configuration } from './configuration';
import type { AxiosPromise, AxiosInstance, AxiosRequestConfig } from 'axios';
import globalAxios from 'axios';
// Some imports not used depending on template conditions
// @ts-ignore
import { DUMMY_BASE_URL, assertParamExists, setApiKeyToObject, setBasicAuthToObject, setBearerAuthToObject, setOAuthToObject, setSearchParams, serializeDataIfNeeded, toPathString, createRequestFunction } from './common';
import type { RequestArgs } from './base';
// @ts-ignore
import { BASE_PATH, COLLECTION_FORMATS, BaseAPI, RequiredError, operationServerMap } from './base';

/**
 * 
 * @export
 * @interface COABase
 */
export interface COABase {
    /**
     * 
     * @type {string}
     * @memberof COABase
     */
    'id': string;
}
/**
 * 
 * @export
 * @interface HTTPValidationError
 */
export interface HTTPValidationError {
    /**
     * 
     * @type {Array<ValidationError>}
     * @memberof HTTPValidationError
     */
    'detail'?: Array<ValidationError>;
}
/**
 * 
 * @export
 * @interface ValidationError
 */
export interface ValidationError {
    /**
     * 
     * @type {Array<ValidationErrorLocInner>}
     * @memberof ValidationError
     */
    'loc': Array<ValidationErrorLocInner>;
    /**
     * 
     * @type {string}
     * @memberof ValidationError
     */
    'msg': string;
    /**
     * 
     * @type {string}
     * @memberof ValidationError
     */
    'type': string;
}
/**
 * 
 * @export
 * @interface ValidationErrorLocInner
 */
export interface ValidationErrorLocInner {
}

/**
 * CoaApi - axios parameter creator
 * @export
 */
export const CoaApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary Get Coas
         * @param {string} id 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getCoasCoaGet: async (id: string, options: AxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'id' is not null or undefined
            assertParamExists('getCoasCoaGet', 'id', id)
            const localVarPath = `/coa`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options};
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            if (id !== undefined) {
                localVarQueryParameter['id'] = id;
            }


    
            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = {...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers};

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * CoaApi - functional programming interface
 * @export
 */
export const CoaApiFp = function(configuration?: Configuration) {
    const localVarAxiosParamCreator = CoaApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary Get Coas
         * @param {string} id 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getCoasCoaGet(id: string, options?: AxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<Array<COABase>>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getCoasCoaGet(id, options);
            const index = configuration?.serverIndex ?? 0;
            const operationBasePath = operationServerMap['CoaApi.getCoasCoaGet']?.[index]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, operationBasePath || basePath);
        },
    }
};

/**
 * CoaApi - factory interface
 * @export
 */
export const CoaApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = CoaApiFp(configuration)
    return {
        /**
         * 
         * @summary Get Coas
         * @param {string} id 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getCoasCoaGet(id: string, options?: any): AxiosPromise<Array<COABase>> {
            return localVarFp.getCoasCoaGet(id, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * CoaApi - object-oriented interface
 * @export
 * @class CoaApi
 * @extends {BaseAPI}
 */
export class CoaApi extends BaseAPI {
    /**
     * 
     * @summary Get Coas
     * @param {string} id 
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof CoaApi
     */
    public getCoasCoaGet(id: string, options?: AxiosRequestConfig) {
        return CoaApiFp(this.configuration).getCoasCoaGet(id, options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * NineLineApi - axios parameter creator
 * @export
 */
export const NineLineApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary Create
         * @param {File} audioFile 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createNinelineCreatePost: async (audioFile: File, options: AxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'audioFile' is not null or undefined
            assertParamExists('createNinelineCreatePost', 'audioFile', audioFile)
            const localVarPath = `/nineline/create`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options};
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;
            const localVarFormParams = new ((configuration && configuration.formDataCtor) || FormData)();


            if (audioFile !== undefined) { 
                localVarFormParams.append('audio_file', audioFile as any);
            }
    
    
            localVarHeaderParameter['Content-Type'] = 'multipart/form-data';
    
            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = {...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers};
            localVarRequestOptions.data = localVarFormParams;

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary Get
         * @param {string} [id] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getNinelineGet: async (id?: string, options: AxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/nineline`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options};
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            if (id !== undefined) {
                localVarQueryParameter['id'] = id;
            }


    
            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = {...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers};

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * NineLineApi - functional programming interface
 * @export
 */
export const NineLineApiFp = function(configuration?: Configuration) {
    const localVarAxiosParamCreator = NineLineApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary Create
         * @param {File} audioFile 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async createNinelineCreatePost(audioFile: File, options?: AxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<void>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.createNinelineCreatePost(audioFile, options);
            const index = configuration?.serverIndex ?? 0;
            const operationBasePath = operationServerMap['NineLineApi.createNinelineCreatePost']?.[index]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, operationBasePath || basePath);
        },
        /**
         * 
         * @summary Get
         * @param {string} [id] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getNinelineGet(id?: string, options?: AxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<void>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getNinelineGet(id, options);
            const index = configuration?.serverIndex ?? 0;
            const operationBasePath = operationServerMap['NineLineApi.getNinelineGet']?.[index]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, operationBasePath || basePath);
        },
    }
};

/**
 * NineLineApi - factory interface
 * @export
 */
export const NineLineApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = NineLineApiFp(configuration)
    return {
        /**
         * 
         * @summary Create
         * @param {File} audioFile 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createNinelineCreatePost(audioFile: File, options?: any): AxiosPromise<void> {
            return localVarFp.createNinelineCreatePost(audioFile, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary Get
         * @param {string} [id] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getNinelineGet(id?: string, options?: any): AxiosPromise<void> {
            return localVarFp.getNinelineGet(id, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * NineLineApi - object-oriented interface
 * @export
 * @class NineLineApi
 * @extends {BaseAPI}
 */
export class NineLineApi extends BaseAPI {
    /**
     * 
     * @summary Create
     * @param {File} audioFile 
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof NineLineApi
     */
    public createNinelineCreatePost(audioFile: File, options?: AxiosRequestConfig) {
        return NineLineApiFp(this.configuration).createNinelineCreatePost(audioFile, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary Get
     * @param {string} [id] 
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof NineLineApi
     */
    public getNinelineGet(id?: string, options?: AxiosRequestConfig) {
        return NineLineApiFp(this.configuration).getNinelineGet(id, options).then((request) => request(this.axios, this.basePath));
    }
}



