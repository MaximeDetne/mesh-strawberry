import {
  defineConfig as defineComposeConfig,
  loadGraphQLHTTPSubgraph,
} from "@graphql-mesh/compose-cli";

export const composeConfig = defineComposeConfig({
  subgraphs: [
    {
      sourceHandler: loadGraphQLHTTPSubgraph("Strawberry API", {
        endpoint: "http://localhost:8000",
      }),
    },
  ],
});
