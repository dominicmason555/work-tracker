<template>
    <div id="editor-pane">
        <div id="top">
            <button>New Task</button>
            <hr>
        </div>
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
            this.$root.$on("note-open", this.openNote);
        },
        methods: {
            setup() {
                this.editor = HyperMD.fromTextArea(document.getElementById("myTextarea"));
                this.editor.setValue("## Open a tasks notes from the left using the arrow button \n");
                this.editor.setSize("100%", "100%");
            },
            async openNote(noteID: number) {
                const response = await fetch(`http://localhost:8000/tasks/${noteID}/notes/`);
                if (response.status === 200) {
                    this.editor.setValue(await response.text());
                }
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
