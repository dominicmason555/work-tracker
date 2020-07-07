<template>
    <div id="taskItem">
        <h2>{{ name }}</h2>
        Added: {{ addedStr }}
        <br>
        {{ startedStr }}
        <br>
        {{ endedStr }}
    </div>
</template>

<script>
    const dateFormat = {weekday: "long", year: "numeric", month: "long", day: "numeric"};

    export default {
        name: "TaskItem",
        props: {
            name: String,
            status: Number,
            parent_id: Number,
            id: Number,
            added: String,
            started: String,
            ended: String,
        },
        data() {
            return {
                startedDate: null,
                startedStr: "Not Started",
                addedDate: null,
                addedStr: "",
                endedDate: null,
                endedStr: "Ongoing",
            };
        },
        created() {
            if (this.started) {
                this.startedDate = new Date(this.started);
                this.startedStr = "Started: " + this.startedDate.toLocaleString("en-GB", dateFormat);
            }
            if (this.added) {
                this.addedDate = new Date(this.added);
                this.addedStr = this.addedDate.toLocaleString("en-GB", dateFormat);
            }
            if (this.status === 1) {
                this.endedStr = "Finished";
                if (this.ended) {
                    this.endedDate = new Date(this.ended);
                    this.endedStr += ": " + this.endedDate.toLocaleString("en-GB", dateFormat);
                }
            }
            if (this.status === 2) {
                this.endedStr = "Cancelled";
                if (this.ended) {
                    this.endedDate = new Date(this.ended);
                    this.endedStr += ": " + this.endedDate.toLocaleString("en-GB", dateFormat);
                }
            }
        },
    };
</script>

<style scoped>
    #taskItem {
        background: #304457;
        padding: 1vh;
        margin-right: 3vh;
        margin-top: 1vh;
        font-size: 11pt;
        text-align: right;
    }

    h2 {
        text-align: left;
        margin: 0;
        font-size: 15pt;
        font-weight: 600;
    }

</style>
