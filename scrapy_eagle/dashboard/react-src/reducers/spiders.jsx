import { Record, OrderedMap } from 'immutable';

const SpiderRecord = Record({
  frequency_minutes: undefined,
  last_started_at: undefined,
  max_concurrency: undefined,
  min_concurrency: undefined,
  max_memory_mb: undefined,
  priority: 0
});

class SpiderInfo extends SpiderRecord {
  getPriority(){
    return this.priority;
  }
}

const SpidersMap = OrderedMap({});

//export const INCREASE_SERVER = 'INCREASE_SERVER';
//export const SET_SERVER_QTY = 'SET_SERVER_QTY';

export default (state = SpidersMap, action) => {

  switch (action.type) {

    case 'UPDATE_SPIDER_INFO':

      // Check if there's already one Record from this Spider
      if(!state.has(action.spider_id)){
        state = state.set(action.spider_id, new SpiderInfo());
      }

      return state.update(action.spider_id,
        (spider_record) =>
          spider_record.merge({
            'priority': action.priority,
            'frequency_minutes': action.frequency_minutes,
            'last_started_at': action.last_started_at,
            'max_concurrency': action.max_concurrency,
            'min_concurrency': action.min_concurrency,
            'max_memory_mb': action.max_memory_mb
          })
      );

    default:
      return state;
  }
}