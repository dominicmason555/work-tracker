<template>
    <div id="editor-pane">
        <label for="myTextarea"></label>
        <textarea id="myTextarea">
        </textarea>
    </div>
</template>

<script lang="ts">
    import Vue from "vue";

    const HyperMD = require("hypermd");
    require("codemirror/mode/htmlmixed/htmlmixed");
    require("codemirror/mode/stex/stex");
    require("codemirror/mode/yaml/yaml");
    require("hypermd/powerpack/fold-math-with-katex");
    require("hypermd/powerpack/hover-with-marked");


    export default Vue.extend({
        name: "Editor",
        data() {
            return {
                editor: HyperMD,
            };
        },
        mounted() {
            this.setup();
        },
        methods: {
            setup() {
                this.editor = HyperMD.fromTextArea(document.getElementById("myTextarea"));
                this.editor.setValue("# This is nice text \n $\\sum^N_n \\cos(\\pi \\cdot n)$ ");
                this.editor.setSize("100%", "100%");
            },
        },
    });
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    #editor-pane {
        display: flex;
        height: 100%;
        flex-direction: column;
    }
</style>
