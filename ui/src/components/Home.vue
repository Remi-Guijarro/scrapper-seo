<template>
    <div>
        <div class="card main">
            <div class="card-header">
                Scrapper-SEO
            </div>
            <div class="card-body">
                <div>
                    <input class="search-bar" type="search" placeholder="Search" aria-label="Search" v-model="keyword">
                    <button class="py-2 btn btn-outline-success my-4" type="submit" @click="addKeyword">Add keyword</button>
                </div>  
                <div class="keyword-container">
                    <ul class="keywords">
                        <li v-for="keyword in keywords" :key="keyword.key" class="word">
                            <span class="delete_btn" @click="remove(keyword.key)">x</span>
                            {{keyword.word}}
                        </li>   
                    </ul>
                </div> 
                <div>
                    <button class="py-2 btn btn-outline-success my-4" type="submit" @click="addQuery">Add query</button>
                </div>   
                <div v-for="query in queries" :key="query.key" class="query">
                    <ul class="keywords">
                        <li v-for="keyword in query.keywords" :key="keyword.key" class="word">
                            {{keyword}}
                        </li>
                    </ul>
                </div>                  
            </div>
            <div v-if="hasQueries">
                <button class="py-2 btn btn-outline-success my-4" type="submit" @click="executeQueries">Execute queries</button>
            </div>  
        </div>
        <div v-if="hasResults" class="results">
            <ul class="list-group">
                <li v-for="result in results" :key="result.key" class="list-group-item">
                    <div class="results-keywords"> 
                        keywords :                        
                        <div class="ms-2 me-auto" v-for="word in result.query.keywords" :key="word.key">
                            {{word}}
                        </div>
                    </div>
                    <span class="badge bg-primary rounded-pill">count : {{result.result}}</span>
                </li>
            </ul>
        </div>
    </div>    
</template>

<script>
const axios = require('axios');


export default {
    data() { 
        return {
            keyword : '',
            keywords: [],
            queries: [],
            results: []
        }        
    }, 

    methods: {
        addKeyword() {
            if(this.keyword != ''){
                this.keywords.push(
                    {word: this.keyword, key: Math.random()}
                )
            }            
            this.keyword = ''
        }, 

        remove(key) {      
            this.keywords = this.keywords.filter(item => item.key != key)
        },

        addQuery() {
            this.queries.push({
                keywords: this.keywords.map(el => el.word),
                key: Math.random()
            })
            this.keywords = []
        },         

        executeQueries() {
            let queriesCopy = this.queries;
            queriesCopy.forEach(element => {
                axios.post('http://127.0.0.1:5000/search',{
                    keywords: element.keywords
                })
                .then((response) => {
                    this.queries = this.queries.filter(el => el.key != element.key)
                    this.addNewResult(element,response.data)
                })
                .catch((error) => {
                    console.log(error);
                }); 
            });         
        },

        addNewResult(query, data) {
            this.results.push({
                key: Math.random(),
                query: query,
                result: data
            })
        }
    },

    computed: {
        hasQueries() {
            return this.queries.length
        },

        hasResults() {
            return this.results.length
        }
    }
}
</script>

<style>
    .main {
        width: 60%;
        margin: auto;
    }

    .search-bar {
        width: 80%;
        padding: 8px;
        padding-left: 15px;
        padding-right:  15px;
    }

    .keyword-container {
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .keywords {
        margin: auto;
        list-style-type: none;
        display: flex;
        flex-wrap: wrap;
        padding: 0px;
    }

    .word {
        background-color: #0d6efd;
        margin: 20px;
        padding: 10px;
        padding-left: 20px;
        color: white;
        border-radius: 5px;
    }

    .delete_btn {
        float: right;
        padding-left: 5px;
        padding-right: 5px;
        position: relative;
        top: -15px;
        right: -10px;
        color: white;
        background-color: red;
        border-radius: 100%;
        cursor: pointer;
    }

    .query {
        background-color: #e8e1e4;
        border-radius: 15px;
        margin-top: 20px;
        margin-bottom: 20px;
    }

    .results {
        width: 60%;
        margin: auto;
        margin-top: 50px;
    }

    .results-keywords {
        display: block;
    }
</style>    