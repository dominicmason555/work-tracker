<template>
    <div id="app" style="grid-auto-flow: row dense;">
        <div id="button-pane">
            <button>Refresh</button>
            <button>Add</button>
        </div>
        <div id="task-pane">
            <TaskList />
        </div>
        <div id="edit-pane">
            <Editor/>
        </div>
    </div>
</template>

<script lang="ts">
    import Vue from "vue";
    import Editor from "./components/Editor.vue";
    import TaskList from "./components/TaskList.vue";

    export default Vue.extend({
        name: "App",
        components: {
            Editor,
            TaskList,
        },
    });
</script>

<style>

    html, body {
        height: 100%;
        margin: 0;
        background: #304457;
    }

    #app {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        color: #FFFFFF;
        display: grid;
        grid-template-columns: repeat(8, 1fr);
        grid-template-rows: 100%;
        gap: 1vw;
        padding: 1vw;
        height: 100%;
        min-height: 100%;
        box-sizing: border-box;
    }

    #button-pane {
        background: #1D2935;
        padding: 0;
        grid-row: 1;
        grid-column: auto / span 1;
        overflow: auto;
    }

    #task-pane {
        background: #1D2935;
        padding: 0;
        grid-row: 1;
        grid-column: auto / span 3;
        overflow: auto;
    }

    #edit-pane {
        background: #1D2935;
        padding: 0.5vh;
        grid-column: auto / span 5;
        grid-row: 1;
    }

    .CodeMirror {
        color: #ddd;
        background-color: #1D2935;
    }

    .CodeMirror-gutters {
        background-color: #1D2935;
    }

    .CodeMirror-cursor {
        color: #dddddd;

    }

</style>
