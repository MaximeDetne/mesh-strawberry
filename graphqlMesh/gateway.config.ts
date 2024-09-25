import { defineConfig } from "@graphql-hive/gateway";
import { createFetch } from "@whatwg-node/fetch";

export const gatewayConfig = defineConfig({
  port: 4001,
  fetchAPI: createFetch({
    formDataLimits: {
      // Maximum allowed file size (in bytes)
      fileSize: 1000000,
      // Maximum allowed number of files
      files: 10,
      // Maximum allowed size of content (operations, variables etc...)
      fieldSize: 1000000,
      // Maximum allowed header size for form data
      headerSize: 1000000,
    },
  }),
});
