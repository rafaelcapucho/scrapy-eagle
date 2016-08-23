import { Record, OrderedMap, List } from 'immutable';

const JobRecord = Record({
  frequency_minutes: undefined,
  last_started_at: undefined,
  max_concurrency: undefined,
  min_concurrency: undefined,
  max_memory_mb: undefined,
  priority: 0,
  type: undefined, // 'spider' or 'command'
  start_urls: new List()
});

class JobInfo extends JobRecord {
  getPriority(){
    return this.priority;
  }
}

const SpidersMap = OrderedMap({});

export default (state = SpidersMap, action) => {

  switch (action.type) {

    case 'UPDATE_SPIDER_INFO':

      // Check if there's already one Record from this Spider
      if(!state.has(action.spider_id)){
        state = state.set(action.spider_id, new JobInfo());
      }

      return state.update(action.spider_id,
        (spider_record) =>
          spider_record.merge({
            'priority': action.priority,
            'frequency_minutes': action.frequency_minutes,
            'last_started_at': action.last_started_at,
            'max_concurrency': action.max_concurrency,
            'min_concurrency': action.min_concurrency,
            'max_memory_mb': action.max_memory_mb,
            'type': action.type,
            'start_urls': action.start_urls
          })
      );

    default:
      return state;
  }
}