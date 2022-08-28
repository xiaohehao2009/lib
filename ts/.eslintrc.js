module.exports = {
    env: {
        es2021: true,
        node: true
    },
    extends: ["airbnb-base"],
    parser: "@typescript-eslint/parser",
    parserOptions: {
        ecmaVersion: "latest",
        sourceType: "module"
    },
    plugins: ["@typescript-eslint"],
    rules: {
        indent: ["error", 4],
        quotes: ["error", "double"],
        "comma-dangle": ["error", "never"],
        "linebreak-style": ["error", "windows"],
        "no-plusplus": ["off"],
        "import/extensions": ["off"],
        "no-console": ["off"],
        radix: ["off"]
    },
    settings: {
        "import/resolver": {
            node: {
                extensions: [".js", ".jsx", ".ts", "vue"]
            }
        }
    }
};
