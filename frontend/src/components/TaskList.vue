<template>
    <div id="taskList">
        <button v-on:click="fetchTasks()">Refresh Tasks</button>
        <ul v-for="task in shownTasks" :key="task.id">
            <TaskItem
                    :name="task.name"
                    :added="task.added"
                    :started="task.started"
                    :ended="task.ended"
                    :id="task.id"
                    :parent_id="task.parent_id"
                    :status="task.status"
            ></TaskItem>
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
                taskMap: new Map(),
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
                    this.taskMap = this.makeTree();
                    this.showAll();
                }
            },
            showAll() {
                this.shownTasks = Array.from(this.tasks);
            },
            makeTree() {
                const levels = [];
                let added = 0;
                let currentLevel = 0;
                const taskMap = new Map();

                // Assemble main map
                this.tasks.forEach((item) => {
                    item.children = [];
                    item.orphaned = false;
                    taskMap.set(item.id, item);
                });

                // Assemble level 0: roots and orphans, also mar k orphans
                levels.push(new Map());
                for (const [id, item] of taskMap) {
                    if (!taskMap.has(item.parent_id)) {
                        if (item.parent_id !== null) {
                            item.orphaned = true;
                        }
                        levels[0].set(id, null);
                        added++;
                    }
                }

                // Assemble deeper levels of children maps from the top down
                while (added > 0) {
                    const currentMap = new Map();
                    currentLevel++;
                    added = 0;
                    for (const [id, item] of taskMap) {
                        if (levels[currentLevel - 1].has(item.parent_id)) {
                            currentMap.set(id, item.parent_id);
                            added++;
                        }
                    }
                    if (added > 0) {
                        levels.push(currentMap);
                    }
                }

                // Add children to parents from bottom of levels upwards and remove from main map
                for (let i = levels.length - 1; i > 0; i--) {
                    for (const [id, parent_id] of levels[i]) {
                        taskMap.get(parent_id).children.push(taskMap.get(id));
                        taskMap.delete(id);
                    }
                }

                console.log(levels);
                console.log(taskMap);
                return taskMap;
            },
        },
    };
</script>

<style scoped>
    #taskList {
        padding: 0;
    }
</style>
