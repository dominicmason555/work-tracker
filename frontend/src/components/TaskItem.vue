<template>
    <div id="taskItem">
        <div id="top">
            <div id="name" @click="select">
                {{ open ? "&darr;" : "&rarr;" }}
                {{ details.name }}
                <button> &gt;</button>
            </div>
            <div id="details" v-show="open">Hello there</div>
        </div>

        <ul v-show="childrenOpen" v-for="task in details.children" :key="task.id">
            <TaskItem :details="task"/>
        </ul>
    </div>
</template>

<script>
    const dateFormat = {weekday: "long", year: "numeric", month: "long", day: "numeric"};

    export default {
        name: "TaskItem",
        props: {
            details: Object,
        },
        data() {
            return {
                open: false,
                childrenOpen: true,
            };
        },
        methods: {
            select() {
                this.open = !this.open;
            },
        },
    };
</script>

<style scoped>
    #top  {
        background: #304457;
        margin: 1vh;
        padding: 7px;
        font-size: 11pt;
        font-weight: bold;
    }

    #top button {
        float: right;
        font-weight: bold;
    }

    #details {
        font-weight: normal;
        font-size: 10pt;
    }

    ul {
        padding-left: 20px;
    }

</style>
