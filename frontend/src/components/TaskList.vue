<template>
    <div id="taskList">
        <button v-on:click="fetchTasks()">Refresh Tasks</button>
        <ul v-for="task in shownTasks" :key="task.id">
            <TaskItem :name=task.name
                      :added=task.added
                      :started=task.started
                      :ended=task.ended
                      :id=task.id
                      :parent_id=task.parent_id
                      :status=task.status>
            </TaskItem>
        </ul>
    </div>
</template>

<script>
    import TaskItem from "./TaskItem.vue";

    export default {
        name: "TaskList",
        components: {
            TaskItem,
        },
        data() {
            return {
                tasks: [],
                shownTasks: [],
            };
        },
        mounted() {
            this.fetchTasks();
        },
        methods: {
            async fetchTasks(update = true) {
                const response = await fetch("http://localhost:8000/tasks");
                this.tasks = await response.json();
                if (update) {
                    this.showAll();
                }
            },
            showAll() {
                this.shownTasks = Array.from(this.tasks);
            },
        },
    };
</script>

<style scoped>
    #taskList {
        padding: 0;
    }
</style>
