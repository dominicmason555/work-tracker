<template>
    <div id="taskItem">
        <div id="top">
            <div id="titleRow">
                <div id="name" ref="name" @click="select" @mouseover="hover(true)" @mouseleave="hover(false)">
                    {{ open ? "&darr;" : "&rarr;" }}
                    {{ details.name }}
                    {{ details.status === 1 ? "&check;" : "" }}
                    <button v-on:click="onArrButton"> &gt;</button>
                </div>
            </div>
            <div id="details" v-show="open">
                <table>
                    <tr>
                        <th> Added:</th>
                        <td> {{added}}</td>
                    </tr>
                    <tr>
                        <th> Started:</th>
                        <td> {{started}}</td>
                    </tr>
                    <tr>
                        <th> {{details.status === 2 ? "Cancelled:" : "Ended:"}}</th>
                        <td> {{ended}}</td>
                    </tr>

                </table>
                <div id="actions">
                    <table>
                        <tr>
                            <td>
                                <button :disabled="details.started != null">Start</button>
                            </td>
                            <td>
                                <button :disabled="details.ended != null">Cancel</button>
                            </td>
                            <td>
                                <button :disabled="details.ended != null">Finish</button>
                            </td>
                            <td>
                                <button v-on:click="onEditButton">Edit</button>
                            </td>
                        </tr>
                    </table>
                </div>
            </div>
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
                hovered: false,
                open: false,
                childrenOpen: true,
            };
        },
        computed: {
            added() {
                return new Date(this.details.added).toLocaleDateString("en-GB", dateFormat).toString();
            },
            started() {
                if (this.details.started === null) {
                    return "Not started";
                } else {
                    return new Date(this.details.started).toLocaleDateString("en-GB", dateFormat).toString();
                }
            },
            ended() {
                if (this.details.ended === null) {
                    return "Not finished";
                } else {
                    return new Date(this.details.ended).toLocaleDateString("en-GB", dateFormat).toString();
                }
            },
        },
        mounted() {
            this.$root.$on("note-open", (id) => {
                if (id !== this.details.id) {
                    this.open = false;
                }
            });
        },
        methods: {

            select() {
                this.open = !this.open;
            },
            onArrButton() {
                setTimeout(() => {
                    this.open = true;
                }, 1);
                this.$root.$emit("note-open", this.details.id);
            },
            hover(isHovered) {
                this.hovered = isHovered;
                if (isHovered) {
                    this.$refs.name.style["text-decoration"] = "underline";
                } else {
                    this.$refs.name.style["text-decoration"] = "none";
                }
            },
            onEditButton() {
                this.$root.$emit("item-edit", this.details.id);
            },
        },
    };
</script>

<style scoped>
    #top {
        background: #304457;
        margin: 1vh;
        padding: 7px;
        font-size: 11pt;
        font-weight: bold;
    }

    #titleRow {
        display: inline-list-item;
        font-weight: bold;
        overflow: auto;
    }

    #name button {
        font-weight: bold;
        float: right;
        font-size: 18px;
        color: #454545;
        text-align: center;
        background: #ecf0f1;
        border: 0;
        border-bottom: 2px solid #dadedf;
        cursor: pointer;
        box-shadow: inset 0 -2px #dadedf;
    }

    #details {
        font-weight: normal;
        font-size: 10pt;
    }

    #details table {
        width: 100%;
        border-spacing: 5px;
    }

    #actions table {
        border-spacing: 5px;
        width: auto;
        margin-left: auto;
        margin-right: auto;
    }

    #details td {
        text-align: right;
    }

    #details th {
        text-align: right;
    }

    ul {
        padding-left: 20px;
    }

</style>
